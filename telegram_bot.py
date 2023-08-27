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
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--seconds_sleep", type=int, help="Enter seconds to sleep", default=os.getenv("TIME_SLEEP"))
arg = parser.parse_args()
seconds_sleep = arg.seconds_sleep
list_files = []
while True:
    list_count = len(list_files)
    if list_count > 0:
        put = 'NewImages/' + list_files[0]
        bot.send_document(chat_id='@NASA_images_2023', document=open(put, 'rb'))
        del list_files[0]
        time.sleep(seconds_sleep)
    else:
        for root, dirs, list_files in os.walk('NewImages/'):
            random.shuffle(list_files)               





# Задача 17.Опубликуйте текст в Telegram-канал
# bot.send_message(chat_id='@NASA_images_2023', text="I'm sorry Dave I'm afraid I can't do that.")
