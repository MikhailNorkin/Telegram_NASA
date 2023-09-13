# Задание 13. Оформите скачивание фотографий в независимые скрипты

import requests
import os
import download
from urllib.parse import urlsplit
from dotenv import load_dotenv


def get_nasa_pictures(api_token):
    url = 'https://api.nasa.gov/planetary/apod'
    query_params = {'api_key': api_token, 'count': '30'}
    response = requests.get(url, params=query_params)
    return response.json()


def main():
    load_dotenv()
    folder_name = "NewImages"
    os.makedirs(folder_name, exist_ok=True)
    api_token = os.getenv("API_KEY_NASA")
    nasa_pictures = get_nasa_pictures(api_token)
    for jpg_number, jpg_url in enumerate(nasa_pictures):
        media_type = jpg_url['media_type']
        if media_type != 'image':
            continue
        jpg_url_name = jpg_url['url']
        url_split = urlsplit(jpg_url_name)
        extension_url = os.path.splitext(url_split[2])[1]
        file_name = "spacex {jpg_number} {extension_url}".format(jpg_number=jpg_number, extension_url=extension_url)
        path_file = os.path.join(folder_name, file_name)
        download.download_image(jpg_url_name, path_file)


if __name__ == '__main__':
    main()