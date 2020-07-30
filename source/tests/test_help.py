from telethon.tl.custom.message import Message
from telethon                   import TelegramClient
from pytest                     import mark


@mark.asyncio
async def test_handle_photo_msg(client: TelegramClient):
    # Create a conversation
    print('here is tests are continue')
    async with client.conversation("@audio_dot_bot", timeout=5) as conv:
        # Send a command
        await conv.send_message(open('tests/static/photo/test_image.jpg', 'rb'))
        # Get response
        resp: Message = await conv.get_response()
        # Make assertions
        assert "@audio_dot_bot" in resp.raw_text
        assert "👍" in resp.raw_text
        assert "👎" in resp.raw_text
