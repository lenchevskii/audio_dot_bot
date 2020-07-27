from telethon.sessions  import StringSession
from telethon.sync      import TelegramClient
from os                 import environ


api_id = int(environ["TELEGRAM_APP_ID"])
api_hash = environ["TELEGRAM_APP_HASH"]

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Your session string is:", client.session.save())
