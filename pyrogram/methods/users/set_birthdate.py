#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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

from typing import Optional

import pyrogram
from pyrogram import raw, types


class SetBirthdate:
    async def set_birthdate(
        self: "pyrogram.Client",
        birthdate: Optional["types.Birthdate"] = None
    ) -> bool:
        """Changes the birthdate of the current user 

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            birthdate (:obj:`~pyrogram.types.Birthdate`, *optional*):
                The new value of the current user's birthdate; pass None to remove the birthdate

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Update your birthdate
                await app.set_birthdate(birthdate=types.Birthdate(
                    day=15,
                    month=12,
                    year=2017
                ))

                # Remove your birthdate
                await app.set_birthdate()

        """

        return bool(
            await self.invoke(
                raw.functions.account.UpdateBirthday(
                    birthday=birthdate.write() if birthdate else None
                )
            )
        )
