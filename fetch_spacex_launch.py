import argparse
import os
import requests


def get_image(url, path, params=None):
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_links(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/latest"
    link_list = get_links(url)
    for number in range(len(link_list)):
        get_image(
            link_list[number],
            os.path.join("images", f"spacex_{number}.jpeg.jpg")
        )


def fetch_spacex_launch(id):
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    link_list = get_links(url)
    for number in range(len(link_list)):
        get_image(
            link_list[number],
            os.path.join("images", f"spacex_{number}.jpeg.jpg")
        )


def main():
    parser = argparse.ArgumentParser(description='Скачивает изображение запуска')
    parser.add_argument('--launch_id', help="ID запуска")
    launch_id = parser.parse_args()
    try:
        fetch_spacex_launch(launch_id.launch_id)
    except requests.exceptions.HTTPError:
        fetch_spacex_last_launch()


if __name__ == "__main__":
    main()
