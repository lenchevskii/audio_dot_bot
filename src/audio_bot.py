from os import makedirs
from os.path import basename, join, exists
from urllib.request import urlopen
from telebot import TeleBot
from setup import TOKEN

bot = TeleBot(TOKEN)


@bot.message_handler(content_types=['voice'])
def handle_voice_msg(message):
    user_id = message.json['from']['id']
    file_id = message.json['voice']['file_id']
    data = urlopen(bot.get_file_url(file_id)).read()
    target_path = join("voices", str(user_id))
    if not exists(target_path):
        makedirs(target_path)
    with open(join(target_path, basename(bot.get_file(file_id).file_path)),
              'wb') as f:
        f.write(data)


bot.polling(timeout=20)
