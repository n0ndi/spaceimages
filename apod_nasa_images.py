import requests
import os
from dotenv import load_dotenv


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


def main():
    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    get_apod_nasa(nasa_token)



if __name__ == "__main__":
    main()