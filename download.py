import requests


def download_image(jpg_url_name, file_path, params=""):

    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
    response = requests.get(jpg_url_name, headers=headers, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)