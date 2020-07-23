import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# Your API ID, hash and session string here
api_id = int(os.environ["TELEGRAM_APP_ID"])
api_hash = os.environ["TELEGRAM_APP_HASH"]
session_str = os.environ["TELETHON_SESSION"]


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


if __name__ == '__main__':
    client()