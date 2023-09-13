import telegram
import time
import os
import argparse
import random
from dotenv import load_dotenv


# Задача 19. Публикуйте фотографии автоматически
load_dotenv()
token = os.getenv("TOKEN_TELEGRAM")
bot = telegram.Bot(token=token)
parser = argparse.ArgumentParser(description='Uploading images to telegram bot @NASA_images_2023')
parser.add_argument("-s", "--seconds_sleep", type=int, help="Enter seconds to sleep", default=os.getenv("TIME_SLEEP"))
arg = parser.parse_args()
seconds_sleep = arg.seconds_sleep
files_nasa = []
while True:
    list_count = len(files_nasa)
    if list_count > 0:
        patch_image = """NewImages/{files_nasa}""".format(files_nasa=files_nasa[0])
        bot.send_document(chat_id='@NASA_images_2023', document=open(patch_image, 'rb'))
        del files_nasa[0]
        time.sleep(seconds_sleep)
    else:
        for root, dirs, files_nasa in os.walk('NewImages/'):
            random.shuffle(files_nasa)               

