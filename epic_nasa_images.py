import time

import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from download_image_func import download_image

def get_epic_nasa(api, path="images"):
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
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/jpg/{images_json[number]['image']}.jpg",
            os.path.join(path, f"_nasa_epic_{number}.jpg"),
            params
        )


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    images_path = os.getenv("IMAGES_PATH", default="images")
    get_epic_nasa(nasa_token, images_path)


if __name__ == "__main__":
    main()
