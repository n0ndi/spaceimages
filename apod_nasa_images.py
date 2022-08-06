import requests
import os
from dotenv import load_dotenv
from get_image_func import get_image


def get_apod_nasa(api, path="images"):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 40,
        "api_key": api
    }
    response = requests.get(url, params)
    response.raise_for_status()
    for number in range(len(response.json())):
        try:
            expansion = os.path.splitext(response.json()[number]["hdurl"])[1]
        except KeyError:
            pass
        if expansion == ".jpg":
            try:
                get_image(
                    response.json()[number]["hdurl"],
                    os.path.join(path, f"_nasa_apod_{number}.jpg"),
                    params
                )
            except KeyError:
                pass
        else:
            pass


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    images_path = os.getenv("IMAGES_PATH")
    get_apod_nasa(nasa_token)



if __name__ == "__main__":
    main()
