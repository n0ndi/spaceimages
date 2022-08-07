import argparse
import os
import dotenv
import requests
from download_image_func import download_image


def get_links(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_launchs(launch_id="latest", path="images"):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    link_list = get_links(url)
    for number in range(len(link_list)):
        download_image(
            link_list[number],
            os.path.join(path, f"spacex_{number}.jpg")
        )


def main():
    dotenv.load_dotenv()
    images_path = os.getenv("IMAGES_PATH", default="images")
    os.makedirs(images_path, exist_ok=True)
    parser = argparse.ArgumentParser(description='Скачивает изображение запуска')
    parser.add_argument('--launch_id', help="ID запуска")
    launch_id = parser.parse_args()
    fetch_spacex_launchs(launch_id.launch_id)


if __name__ == "__main__":
    main()
