import argparse
import os
import requests
from dotenv import load_dotenv
from download_image_func import download_image


def get_apod_nasa(api, path, count):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": count,
        "api_key": api
    }
    response = requests.get(url, params)
    response.raise_for_status()
    images_json = response.json()
    for number, image in enumerate(images_json):
        try:
            extension = os.path.splitext(image["hdurl"])[1]
        except KeyError:
            continue
        if extension == ".jpg":
                download_image(
                    image["hdurl"],
                    os.path.join(path, f"_nasa_apod_{number}.jpg"),
                    params
                )


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    images_path = os.getenv("IMAGES_PATH", default="images")
    os.makedirs(images_path, exist_ok=True)
    parser = argparse.ArgumentParser(description='Скачивает изображение дня NASA')
    parser.add_argument('--count', help="кол-во фотографий", default="30", type=int)
    images_count = parser.parse_args()
    get_apod_nasa(nasa_token, images_path, images_count.count)


if __name__ == "__main__":
    main()
