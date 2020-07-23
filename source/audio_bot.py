from modules.face_detection.face_detect import has_face
from urllib.request                     import urlopen
from urllib.parse                       import urlparse
from subprocess                         import call
from os.path                            import basename, join, exists, splitext
from telebot                            import TeleBot, apihelper
from setup                              import TOKEN
from os                                 import makedirs

apihelper.proxy = {'http': '144.217.101.245:3129'}

bot = TeleBot(TOKEN)


def convert_to_wav(url, target_directory):
    call(
        ' '.join(['ffmpeg', '-i', url, '-ar', '16000',
                  ''.join([target_directory, "/",
                           splitext(basename(urlparse(url).path))[0],
                           ".wav"])]),
        shell=True
    )


@bot.message_handler(content_types=['voice'])
def handle_voice_msg(message):
    user_id = message.json['from']['id']
    file_id = message.json['voice']['file_id']
    file_url = bot.get_file_url(file_id)
    target_directory = join("static", "voice", str(user_id))

    if not exists(target_directory):
        makedirs(target_directory)
        convert_to_wav(file_url, target_directory)


@bot.message_handler(content_types=['photo'])
def handle_photo_msg(message):
    user_id = message.json['from']['id']
    file_id = message.json['photo'][-1]['file_id']
    data = urlopen(bot.get_file_url(file_id)).read()

    if has_face(data):
        target_directory = join("static", "photo", str(user_id))
        data_path = join(target_directory,
                         basename(bot.get_file(file_id).file_path))
        if not exists(data_path):
            makedirs(target_directory)
            with open(data_path, 'wb') as f:
                f.write(data)


bot.polling(timeout=20)
