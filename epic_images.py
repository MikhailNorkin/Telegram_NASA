# Задание 13. Оформите скачивание фотографий в независимые скрипты

import requests
import os
import urllib.parse
import json
import argparse
import download
import datetime as DT
from dotenv import load_dotenv


def fetch_nasa_day(file_name, url, token):
    folder_name = "NewImages11"
    os.makedirs(folder_name, exist_ok=True) 
    new_path = os.path.join(folder_name, file_name)
    payload = {"api_key": token}
    download.download_image(url, new_path, payload)


def main():
    parser = argparse.ArgumentParser(description='Image search on nasa.gov...')
    parser.add_argument("-d", "--data_launch", type=str, help="Enter launch data (yyyy-mm-dd)", default="2020-12-25")
    arg = parser.parse_args()
    data_launch = DT.datetime.strptime(arg.data_launch, '%Y-%m-%d').date()
    load_dotenv()
    token = os.getenv("TOKEN_NASA")
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = urllib.parse.urlencode({'date': data_launch, 'api_key': token})
    response = requests.get(url, params=params)
    nasa_pictures = json.loads(response.text)
    for jpg_number, jpg_url in enumerate(nasa_pictures):
        url = 'https://api.nasa.gov/EPIC/archive/natural/'
        for data_part in jpg_url['date'].split(' ')[0].split('-'):
            url = """{url}{data_part}/""".format(url=url, data_part=data_part)
        url = """{url}png/{jpg_url}.png""".format(url=url, jpg_url=jpg_url['image'])
        file_name = """spacex{jpg_number}.png""".format(jpg_number=str(jpg_number))
        fetch_nasa_day(file_name, url, token)


if __name__ == '__main__':
    main()