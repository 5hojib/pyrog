Available Methods
=================

This page is about Pyrogram methods. All the methods listed here are bound to a :class:`~pyrogram.Client` instance,
except for :meth:`~pyrogram.idle()` and :meth:`~pyrogram.compose()`, which are special functions that can be found in
the main package directly.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    with app:
        app.send_message(chat_id="me", text="hi")

-----

.. currentmodule:: pyrogram.Client

Utilities
---------

.. autosummary::
    :nosignatures:

    {utilities}

.. toctree::
    :hidden:

    {utilities}

.. currentmodule:: pyrogram

.. autosummary::
    :nosignatures:

    idle
    compose

.. toctree::
    :hidden:

    idle
    compose

.. currentmodule:: pyrogram.Client

Messages
--------

.. autosummary::
    :nosignatures:

    {messages}

.. toctree::
    :hidden:

    {messages}

Chats
-----

.. autosummary::
    :nosignatures:

    {chats}

.. toctree::
    :hidden:

    {chats}

Chat Forum Topics
-----

.. autosummary::
    :nosignatures:

    {chat_topics}

.. toctree::
    :hidden:

    {chat_topics}

Telegram Business
-------------

.. autosummary::
    :nosignatures:

    {business}

.. toctree::
    :hidden:

    {business}

Users
-----

.. autosummary::
    :nosignatures:

    {users}

.. toctree::
    :hidden:

    {users}

Invite Links
------------

.. autosummary::
    :nosignatures:

    {invite_links}

.. toctree::
    :hidden:

    {invite_links}

Contacts
--------

.. autosummary::
    :nosignatures:

    {contacts}

.. toctree::
    :hidden:

    {contacts}

Stickers
--------

.. autosummary::
    :nosignatures:

    {stickers}

.. toctree::
    :hidden:

    {stickers}

Password
--------

.. autosummary::
    :nosignatures:

    {password}

.. toctree::
    :hidden:

    {password}

Phone
--------

.. autosummary::
    :nosignatures:

    {phone}

.. toctree::
    :hidden:

    {phone}

Bots
----

.. autosummary::
    :nosignatures:

    {bots}

.. toctree::
    :hidden:

    {bots}

Authorization
-------------

.. autosummary::
    :nosignatures:

    {authorization}

.. toctree::
    :hidden:

    {authorization}

Advanced
--------

Methods used only when dealing with the raw Telegram API.
Learn more about how to use the raw API at :doc:`Advanced Usage <../../topics/advanced-usage>`.

.. autosummary::
    :nosignatures:

    {advanced}

.. toctree::
    :hidden:

    {advanced}
