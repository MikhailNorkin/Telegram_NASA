# Задание 13. Оформите скачивание фотографий в независимые скрипты

import requests
import os
import urllib.parse
import json
import argparse
import datetime as DT
from dotenv import load_dotenv


def fetch_spacex_day(file_name, url, token):
    new_path = os.path.join('C:/Work/Devman/Telegram_NASA/NewImages11', file_name)
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
    payload = {"api_key": token}
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    with open(new_path, 'wb') as file:
        file.write(response.content)


def main(data_launch):
    load_dotenv()
    token = os.getenv("TOKEN_NASA")
    url = 'https://api.nasa.gov/EPIC/api/natural'
    query_params = {'date': data_launch, 'api_key': token}
    params = urllib.parse.urlencode(query_params)
    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    for jpg_number, jpg_url in enumerate(json_data):
        url = 'https://api.nasa.gov/EPIC/archive/natural/'
        for data_part in jpg_url['date'].split(' ')[0].split('-'):
            url = url + data_part + '/'
        url = url + 'png/' + jpg_url['image'] + '.png'
        file_name = 'spacex' + str(jpg_number) + '.png' 
        fetch_spacex_day(file_name, url, token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data_launch", type=str, help="Enter launch data (yyyy-mm-dd)", default="2020-12-25")
    arg = parser.parse_args()
    data_launch = DT.datetime.strptime(arg.data_launch, '%Y-%m-%d').date()
    main(data_launch)