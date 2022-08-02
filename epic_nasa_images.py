import requests
import os
from dotenv import load_dotenv

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