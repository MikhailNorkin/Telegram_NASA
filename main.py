import requests
import os
from urllib.parse import urlsplit
from urllib.parse import urlparse
import urllib.parse
import json
from dotenv import load_dotenv


# Задание 11. Скачайте EPIC-фото
def fetch_spacex_day(file_name, url, token):
    new_path = os.path.join('C:/Work/Devman/Telegram/NewImages11', file_name)
    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
    payload = {"api_key": token}
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    with open(new_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()
    token = os.getenv("TOKEN_NASA")
    url = 'https://api.nasa.gov/EPIC/api/natural'
    query_params = {'date': '2020-12-25', 'api_key': token}
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
    main()


# url = 'https://api.nasa.gov/EPIC/api/natural'
# API_KEY = 'RzN1PsuZd9ibV2KOiIuqAqDsmTosnjjn53DNIusG'
# query_params = {'date': '2020-12-25', 'api_key': API_KEY}
# params = urllib.parse.urlencode(query_params)
# response = requests.get(url, params=params)
# json_data = json.loads(response.text)
# for jpg_number, jpg_url in enumerate(json_data):
#     url = 'https://api.nasa.gov/EPIC/archive/natural/'
#     for data_part in jpg_url['date'].split(' ')[0].split('-'):
#         url = url + data_part + '/'
#     url = url + 'png/' + jpg_url['image'] + '.png'
#     file_name = 'spacex' + str(jpg_number) + '.png'  
#     new_path = os.path.join('C:/Work/Devman/Telegram/NewImages11', file_name)
#     headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
#     payload = {"api_key": API_KEY}
#     response = requests.get(url, headers=headers, params=payload)
#     response.raise_for_status()
#     with open(new_path, 'wb') as file:
#         file.write(response.content)


# Задание 9. Скачайте много картинок дня
# url = 'https://api.nasa.gov/planetary/apod'
# API_KEY = 'RzN1PsuZd9ibV2KOiIuqAqDsmTosnjjn53DNIusG'
# query_params = {'api_key': API_KEY, 'count': '30'}
# params = urllib.parse.urlencode(query_params)
# response = requests.get(url, params=params)
# json_data = json.loads(response.text)
# for jpg_number, jpg_url in enumerate(json_data):
#     jpg_url_name = jpg_url['url']
#     url_split = urlsplit(jpg_url_name)
#     extension_url = os.path.splitext(url_split[2])[1]
#     file_name = 'spacex' + str(jpg_number) + extension_url
#     new_path = os.path.join('C:/Work/Devman/Telegram/NewImages', file_name)
#     headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
#     response = requests.get(jpg_url_name, headers=headers)
#     response.raise_for_status()
#     with open(new_path, 'wb') as file:
#         file.write(response.content)


# Задание 8. Научитесь скачивать картинки любого расширения
# adres = requests.get('https://api.nasa.gov/planetary/apod?api_key=RzN1PsuZd9ibV2KOiIuqAqDsmTosnjjn53DNIusG')
# response = requests.get(adres.url)
# response.raise_for_status()
# url_split = urlsplit(response.json()['url'])
# extension_url = os.path.splitext(url_split[2])[1]


# Задание 7. Получите ссылку на картинку от NASA
# adres = requests.get('https://api.nasa.gov/planetary/apod?api_key=RzN1PsuZd9ibV2KOiIuqAqDsmTosnjjn53DNIusG')
# response = requests.get(adres.url)
# response.raise_for_status()
# print(response.json()['url'])


# # Задание 6. Оформите скачивание фотографий как функцию
# def fetch_spacex_last_launch():
#     adres = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
#     response = requests.get(adres.url)
#     response.raise_for_status()
#     return response.json()['links']['flickr']['original']


# def main():
#     try:
#         os.makedirs("images")
#     except FileExistsError:
#         pass

#     list_jpgs = fetch_spacex_last_launch()
#     for jpg_number, jpg_url in enumerate(list_jpgs):
#         new_path = os.path.join('C:\Work\Devman\Telegram\images', 'spacex' + str(jpg_number) + '.jpeg')
#         headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
#         response = requests.get(jpg_url, headers=headers)
#         response.raise_for_status()
#         with open(new_path, 'wb') as file:
#             file.write(response.content)


# if __name__ == '__main__':
#     main()


# Задание 5. Скачайте все фотографии с последнего запуска SpaceX
# adres = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
# response = requests.get(adres.url)
# response.raise_for_status()
# list_jpgs = response.json()['links']['flickr']['original']
# for jpg_number, jpg_url in enumerate(list_jpgs):
#     new_path = os.path.join('C:\Work\Devman\Telegram\images', 'spacex' + str(jpg_number) + '.jpeg')
#     headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
#     response = requests.get(jpg_url, headers=headers)
#     response.raise_for_status()
#     with open(new_path, 'wb') as file:
#         file.write(response.content)


# Задание 4. Получите ссылки на фотографии с последнего запуска SpaceX
# adres = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
# response = requests.get(adres.url)
# response.raise_for_status()
# print(response.json()['links']['flickr']['original'])


# Задание 3. Скачайте изображение с помощью Python
# def download_picture(url_picture, folder_address):
#     new_path = os.path.join(folder_address, 'hubble.jpeg')

#     headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
#     response = requests.get(url_picture, headers=headers)
#     response.raise_for_status()

#     with open(new_path, 'wb') as file:
#         file.write(response.content)


# def main():
#     try:
#         os.makedirs("Новая папка")
#     except FileExistsError:
#         pass

#     download_picture("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg", 'C:\Work\Devman\Telegram\Новая папка')


# if __name__ == '__main__':
#     main()
    
    
# Задание 2. Создайте папку для картинок
# try:
#     os.makedirs("Новая папка")
# except FileExistsError:
#     pass

# Задание 1. Скачайте изображение с помощью Python
# filename = 'hubble.jpeg'
# url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

# headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot)'}
# response = requests.get(url, headers=headers)
# response.raise_for_status()

# with open(filename, 'wb') as file:
#     file.write(response.content)