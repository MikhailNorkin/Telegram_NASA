import telegram
import os
import argparse
import random
from dotenv import load_dotenv

# Задача 18. Опубликуйте картинку в Telegram-канал.
# Публикует указанную фотографию в канал. Если “какую” не указано, публикует случайную фотографию.
def main():
    load_dotenv()
    token = os.getenv("TOKEN_TELEGRAM")
    bot = telegram.Bot(token=token)
    parser = argparse.ArgumentParser(description='Uploading image to telegram bot @NASA_images_2023')
    parser.add_argument("-n", "--name_image", type=str, help="Enter name image", default="")
    arg = parser.parse_args()
    image_name = arg.name_image
    if not image_name:
        print("!")
        for root, dirs, list_files in os.walk('NewImages/'):
            random.shuffle(list_files)
            file_path = 'NewImages/' + list_files[0]
    else:
        file_path = 'NewImages/' + image_name
    with open(file_path,'rb') as file_image:
        bot.send_document(chat_id='@NASA_images_2023', document=file_image)
    file_image.closed


if __name__ == '__main__':
    main()