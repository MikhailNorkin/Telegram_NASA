import telegram
import os
import argparse
import random
from dotenv import load_dotenv

# Задача 18. Опубликуйте картинку в Telegram-канал.
# Публикует указанную фотографию в канал. Если “какую” не указано, публикует случайную фотографию.
load_dotenv()
token = os.getenv("TOKEN_TELEGRAM")
bot = telegram.Bot(token=token)
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name_image", type=str, help="Enter name image", default="")
arg = parser.parse_args()
name_image = arg.name_image
if name_image == "":
    for root, dirs, list_files in os.walk('NewImages/'):
        random.shuffle(list_files)
        file_path = 'NewImages/' + list_files[0]
else:
    file_path = 'NewImages/' + name_image
bot.send_document(chat_id='@NASA_images_2023', document=open(file_path, 'rb'))

