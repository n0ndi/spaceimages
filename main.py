import requests
import os
from dotenv import load_dotenv


def get_links():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def get_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    link_list = get_links()
    for number in range(len(link_list)):
        get_image(link_list[number], f"images\spacex_{number}.jpeg")


def get_apod_nasa(api):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 40,
        "api_key": api
    }
    response = requests.get(url, params)
    response.raise_for_status()
    for number in range(len(response.json())):
        expansion = os.path.splitext(response.json()[number]["hdurl"])[1]
        if expansion == ".jpg":
            reply = requests.get(response.json()[number]["hdurl"])
            with open(f"images\_nasa_apod_{number}.jpg", 'wb') as file:
                file.write(reply.content)
        else:
            pass


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
        reply = requests.get(
            f"https://api.nasa.gov/EPIC/archive/natural/{date}/jpg/{response.json()[number]['image']}.jpg", params)
        with open(f"images\_nasa_epic_{number}.jpg", 'wb') as file:
            file.write(reply.content)


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    get_epic_nasa(nasa_token)

if __name__ == "__main__":
    main()