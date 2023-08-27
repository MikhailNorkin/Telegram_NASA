# Задание 13. Оформите скачивание фотографий в независимые скрипты

import requests
import os
import urllib.parse
import json
import download
from urllib.parse import urlsplit
from dotenv import load_dotenv


def main():
    load_dotenv()
    token_API = os.getenv("API_KEY")
    url = 'https://api.nasa.gov/planetary/apod'
    query_params = {'api_key': token_API, 'count': '30'}
    params = urllib.parse.urlencode(query_params)
    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    name_folder = download.folder("NewImages")
    for jpg_number, jpg_url in enumerate(json_data):
        media_type = jpg_url['media_type']
        if media_type == 'image':
            jpg_url_name = jpg_url['url']
            url_split = urlsplit(jpg_url_name)
            extension_url = os.path.splitext(url_split[2])[1]
            file_name = 'spacex' + str(jpg_number) + extension_url
            new_path = os.path.join(name_folder, file_name)
            download.download_image(jpg_url_name, new_path)


if __name__ == '__main__':
    main()