# Задание 13. Оформите скачивание фотографий в независимые скрипты

import argparse
import requests
import os
import download


def fetch_last_launch_spacex(launch):
    url_spacex = f"https://api.spacexdata.com/v5/launches/{launch}"    
    response = requests.get(url_spacex)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    parser = argparse.ArgumentParser(description='Image search on nasa.gov spacexdata.com')
    parser.add_argument("-l", "--launch", type=str, help="Enter the launch number", default="5eb87d47ffd86e000604b38a")
    arg = parser.parse_args()
    print(arg.launch)
    jpgs_spacex = fetch_last_launch_spacex(arg.launch)
    folder_name = "Images"
    os.makedirs(folder_name, exist_ok=True) 
    for jpg_number, jpg_url in enumerate(jpgs_spacex):
        file_name = os.path.join(folder_name, """spacex{jpg_number}.jpeg""".format(jpg_number=jpg_number))
        download.download_image(jpg_url, file_name)


if __name__ == '__main__':
    main()