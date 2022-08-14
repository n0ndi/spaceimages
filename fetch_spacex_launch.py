import argparse
import os
import dotenv
import requests
from download_image_func import download_image
from time import sleep


def get_links(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_launch(launch_id, path):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    link_list = get_links(url)
    for number, link in enumerate(link_list):
        download_image(
            link,
            os.path.join(path, f"spacex_{number}.jpg")
        )


def main():
    dotenv.load_dotenv()
    images_path = os.getenv("IMAGES_PATH", default="images")
    os.makedirs(images_path, exist_ok=True)
    parser = argparse.ArgumentParser(description='Скачивает изображение запуска')
    parser.add_argument('--launch_id', help="ID запуска", default="latest")
    launch_id = parser.parse_args()
    fetch_spacex_launch(launch_id.launch_id, images_path)


if __name__ == "__main__":
    main()
