import requests
import os
from dotenv import load_dotenv
from fetch_spacex_launch import get_image


def get_epic_nasa(api):
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
            os.path.join("images", f"_nasa_epic_{number}.jpg"),
            params
        )


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    get_epic_nasa(nasa_token)


if __name__ == "__main__":
    main()
