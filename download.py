import requests


def download_image(jpg_url_name, new_path):
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
    response = requests.get(jpg_url_name, headers=headers)
    response.raise_for_status()
    with open(new_path, 'wb') as file:
        file.write(response.content)