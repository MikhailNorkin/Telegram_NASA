# Задание 13. Оформите скачивание фотографий в независимые скрипты

import argparse
import requests
import os
import download


def fetch_spacex_last_launch(launch):
    if launch == "":
        adres = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    else:
        adres = requests.get("""https://api.spacexdata.com/v5/launches/+{launch}""".format(launch=launch))
    response = requests.get(adres.url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    parser = argparse.ArgumentParser(description='Image search on nasa.gov spacexdata.com')
    parser.add_argument("-l", "--launch", type=str, help="Enter the launch number", default="")
    arg = parser.parse_args()
    list_jpgs = fetch_spacex_last_launch(arg.launch)
    folder_name = "Images"
    os.makedirs(folder_name, exist_ok=True) 
    for jpg_number, jpg_url in enumerate(list_jpgs):
        new_path = os.path.join(folder_name, """spacex{jpg_number}.jpeg""".format(jpg_number=str(jpg_number)))
        download.download_image(jpg_url, new_path)


if __name__ == '__main__':
    main()