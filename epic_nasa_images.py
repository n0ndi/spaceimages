import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from download_image_func import download_image
from time import sleep


def get_epic_nasa(api, path):
    url = f"https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": api
    }
    response = requests.get(url, params)
    response.raise_for_status()
    images_json = response.json()
    for number, image in enumerate(images_json):
        date = datetime.fromisoformat(image["date"])
        date = '{:%Y/%m/%d}'.format(date)
        download_image(
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/jpg/{image['image']}.jpg",
            os.path.join(path, f"_nasa_epic_{number}.jpg"),
            params
        )


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    images_path = os.getenv("IMAGES_PATH", default="images")
    os.makedirs(images_path, exist_ok=True)
    while True:
        try:
            get_epic_nasa(nasa_token, images_path)
            break
        except requests.exceptions.HTTPError or requests.exceptions.ConnectionError:
            sleep(2)


if __name__ == "__main__":
    main()
