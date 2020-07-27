from telethon.sessions  import StringSession
from telethon           import TelegramClient
from os                 import environ

import pytest

# Your API ID, hash and session string here
api_id = int(environ["TELEGRAM_APP_ID"])
api_hash = environ["TELEGRAM_APP_HASH"]
session_str = environ["TELETHON_SESSION"]


@pytest.fixture(scope="session")
async def client() -> TelegramClient:
    # Connect to the server
    await client.connect()
    # Issue a high level command to start receiving message
    await client.get_me()
    # Fill the entity cache
    await client.get_dialogs()

    yield TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )

    await client.disconnect()
    await client.disconnected
