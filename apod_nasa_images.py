import requests
import os
from dotenv import load_dotenv
from download_image_func import download_image


def get_apod_nasa(api, path="images"):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 40,
        "api_key": api
    }
    response = requests.get(url, params)
    response.raise_for_status()
    images_json = response.json()
    for number, image in enumerate(images_json):
        try:
            extension = os.path.splitext(image["hdurl"])[1]
        except KeyError:
            pass
        if extension == ".jpg":
            try:
                download_image(
                    image["hdurl"],
                    os.path.join(path, f"_nasa_apod_{number}.jpg"),
                    params
                )
            except KeyError:
                continue


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    images_path = os.getenv("IMAGES_PATH", default="images")
    get_apod_nasa(nasa_token)



if __name__ == "__main__":
    main()
