# Задание 13. Оформите скачивание фотографий в независимые скрипты

import requests
import os
import urllib.parse
import json
import download
from urllib.parse import urlsplit
from dotenv import load_dotenv


def get_json():
    API_token = os.getenv("API_KEY")
    url = 'https://api.nasa.gov/planetary/apod'
    query_params = {'api_key': API_token, 'count': '30'}
    response = requests.get(url, params=query_params)
    return response.json()


def main():
    load_dotenv()
    folder_name = download.folder("NewImages")
    json_data = get_json()
    for jpg_number, jpg_url in enumerate(json_data):
        media_type = jpg_url['media_type']
        if media_type == 'image':
            jpg_url_name = jpg_url['url']
            url_split = urlsplit(jpg_url_name)
            extension_url = os.path.splitext(url_split[2])[1]
            file_name = 'spacex' + str(jpg_number) + extension_url
            new_path = os.path.join(folder_name, file_name)
            download.download_image(jpg_url_name, new_path)


if __name__ == '__main__':
    main()