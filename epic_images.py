# Задание 13. Оформите скачивание фотографий в независимые скрипты

import requests
import os
import urllib.parse
import json
import argparse
import download
import datetime as DT
from dotenv import load_dotenv


def download_image_nasa(file_name, url, token):
    folder_name = "NewImages11"
    os.makedirs(folder_name, exist_ok=True) 
    new_path = os.path.join(folder_name, file_name)
    payload = {"api_key": token}
    download.download_image(url, new_path, payload)


def main():
    parser = argparse.ArgumentParser(description='Image search on nasa.gov...')
    parser.add_argument("-d", "--data_launch", type=str, help="Enter launch data (yyyy-mm-dd)", default="2020-12-25")
    arg = parser.parse_args()
    launch_date = DT.datetime.strptime(arg.data_launch, '%Y-%m-%d').date()

    load_dotenv()
    token = os.getenv("TOKEN_NASA")
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = urllib.parse.urlencode({'date': launch_date, 'api_key': token})
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
    nasa_pictures = response.json()

    for jpg_number, jpg_url in enumerate(nasa_pictures):
        url = 'https://api.nasa.gov/EPIC/archive/natural/'
        launch_date = jpg_url['date'].split(' ')[0].replace('-', '/')
        url = """{url}{launch_date}/png/{jpg_url}.png""".format(url=url, launch_date=launch_date, jpg_url=jpg_url['image'])
        file_name = """spacex{jpg_number}.png""".format(jpg_number=jpg_number)
        download_image_nasa(file_name, url, token)


if __name__ == '__main__':
    main()