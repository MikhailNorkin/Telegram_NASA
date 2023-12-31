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
    files_nasa = []
    while True:
        list_count = len(files_nasa)
        if not list_count:
            for root, dirs, files_nasa in os.walk('NewImages/'):
                random.shuffle(files_nasa)   
        else:
            patch_image = """NewImages/{files_nasa}""".format(files_nasa=files_nasa[0])
            with open(patch_image,'rb') as file_image:
                bot.send_document(chat_id='@NASA_images_2023', document=file_image)
            file_image.closed
            del files_nasa[0]
            time.sleep(seconds_sleep)


if __name__ == '__main__':
    main()