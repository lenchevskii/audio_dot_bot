from telethon.tl.custom.message import Message
from telethon                   import TelegramClient
from pytest                     import mark


@mark.asyncio
async def test_help(client: TelegramClient):
    # Create a conversation
    with client.conversation("@audio_dot_bot", timeout=5) as conv:
        # Send a command
        await conv.send_message("/help")
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "@audio_dot_bot" in resp.raw_text
        assert "👍" in resp.raw_text
        assert "👎" in resp.raw_text
