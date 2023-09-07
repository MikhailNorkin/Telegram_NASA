import requests
import os


def download_image(jpg_url_name, path_file):
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
    response = requests.get(jpg_url_name, headers=headers)
    response.raise_for_status()
    with open(path_file, 'wb') as file:
        file.write(response.content)


def folder(name_folder):
    if not os.path.exists(name_folder):
        os.makedirs(name_folder)
    return name_folder