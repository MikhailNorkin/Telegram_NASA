import telegram
import time
import os
import argparse
import random
from dotenv import load_dotenv


# Задача 19. Публикуйте фотографии автоматически
def main():
    load_dotenv()
    token = os.getenv("TOKEN_TELEGRAM")
    bot = telegram.Bot(token=token)
    parser = argparse.ArgumentParser(description='Uploading images to telegram bot @NASA_images_2023')
    parser.add_argument("-s", "--seconds_sleep", type=int, help="Enter seconds to sleep", default=os.getenv("TIME_SLEEP"))
    arg = parser.parse_args()
    seconds_sleep = arg.seconds_sleep
    nasa_files = []
    user_chat_id = os.getenv("CHAT_ID")
    while True:
        list_count = len(nasa_files)
        if not list_count:
            for root, dirs, nasa_files in os.walk('NewImages/'):
                random.shuffle(nasa_files)   
        else:
            patch_image = """NewImages/{nasa_files}""".format(nasa_files=nasa_files[0])
            with open(patch_image,'rb') as file_image:
                bot.send_document(chat_id=user_chat_id, document=file_image)
            del nasa_files[0]
            time.sleep(seconds_sleep)


if __name__ == '__main__':
    main()