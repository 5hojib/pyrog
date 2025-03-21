#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2017-present bakatrouble <https://github.com/bakatrouble>
#  Copyright (C) 2017-present cavallium <https://github.com/cavallium>
#  Copyright (C) 2017-present andrew-ld <https://github.com/andrew-ld>
#  Copyright (C) 2017-present 01101sam <https://github.com/01101sam>
#  Copyright (C) 2017-present KurimuzonAkuma <https://github.com/KurimuzonAkuma>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import logging
import os
import sqlite3
from pathlib import Path

from .sqlite_storage import SQLiteStorage

log = logging.getLogger(__name__)

USERNAMES_SCHEMA = """
CREATE TABLE IF NOT EXISTS usernames
(
    id       INTEGER,
    username TEXT,
    FOREIGN KEY (id) REFERENCES peers(id)
);

CREATE INDEX idx_usernames_username ON usernames (username);
"""

UPDATE_STATE_SCHEMA = """
CREATE TABLE update_state
(
    id   INTEGER PRIMARY KEY,
    pts  INTEGER,
    qts  INTEGER,
    date INTEGER,
    seq  INTEGER
);
"""


class FileStorage(SQLiteStorage):
    FILE_EXTENSION = ".session"

    def __init__(self, name: str, workdir: Path):
        super().__init__(name)

        self.database = workdir / (self.name + self.FILE_EXTENSION)

    def _connect_impl(self, path):
        self.conn = sqlite3.connect(path)
        
        with self.conn:
            self.conn.execute("PRAGMA journal_mode=WAL").close()
            self.conn.execute("PRAGMA synchronous=NORMAL").close()
            self.conn.execute("PRAGMA temp_store=1").close()

    async def update(self):
        version = await self.version()

        if version == 1:
            with self.conn:
                self.conn.execute("DELETE FROM peers")

            version += 1

        if version == 2:
            with self.conn:
                try:
                    self.conn.execute("ALTER TABLE sessions ADD api_id INTEGER")
                except Exception as e:
                    log.exception(e)

            version += 1

        if version == 3:
            with self.conn:
                self.conn.executescript(USERNAMES_SCHEMA)

            version += 1

        if version == 4:
            with self.conn:
                self.conn.executescript(UPDATE_STATE_SCHEMA)

            version += 1

        await self.version(version)

    async def open(self):
        path = self.database
        file_exists = path.is_file()

        self.conn = sqlite3.connect(str(path), timeout=1, check_same_thread=False)

        if not file_exists:
            await self.create()
        else:
            await self.update()

        with self.conn:
            self.conn.execute("VACUUM")

    async def delete(self):
        os.remove(self.database)
