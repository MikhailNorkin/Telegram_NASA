# Задание 13. Оформите скачивание фотографий в независимые скрипты

import argparse
import requests
import os
import download


def fetch_spacex_last_launch(launch):
    if launch == "":
        adres = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    else:
        adres = requests.get('https://api.spacexdata.com/v5/launches/'+launch)
    response = requests.get(adres.url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main(launch):
    list_jpgs = fetch_spacex_last_launch(launch)
    for jpg_number, jpg_url in enumerate(list_jpgs):
        new_path = os.path.join('C:\Work\Devman\Telegram_NASA\images', 'spacex' + str(jpg_number) + '.jpeg')
        download.download_image(jpg_url, new_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--launch", type=str, help="Enter the launch number", default="")
    arg = parser.parse_args()
    main(arg.launch)