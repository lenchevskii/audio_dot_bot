from telebot import TeleBot
from soundfile import read, write

TOKEN = '1258276553:AAHVt-5LwAFnqlvYzm7VdfXtwWn46vXmWQ8'

bot = TeleBot(TOKEN)


@bot.message_handler(content_types=['voice'])
def handle_voice_msg(message):
    user_id = message.json['from']['id']
    file_id = message.json['voice']['file_id']
    data, samplerate = read(bot.get_file_url(file_id))
    print(samplerate)
    write(f'voices/{user_id}/{bot.get_file(file_id)["file_path"]}',
          data,
          samplerate
          )


bot.polling(timeout=20)
