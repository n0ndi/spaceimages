import requests
import os
from dotenv import load_dotenv
from get_image_func import get_image

def get_epic_nasa(api, path="images"):
    url = f"https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": api
    }
    response = requests.get(url, params)
    response.raise_for_status()
    for number in range(10):
        date = (response.json()[number]['date'].split()[0]).split("-")
        date = "/".join(date)
        get_image(
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/jpg/{response.json()[number]['image']}.jpg",
            os.path.join(path, f"_nasa_epic_{number}.jpg"),
            params
        )


def main():
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    images_path = os.getenv("IMAGES_PATH")
    get_epic_nasa(nasa_token, images_path)


if __name__ == "__main__":
    main()
