import argparse
import random
import sys
import telegram
import os
from dotenv import load_dotenv
from time import sleep


def send_image(timer, api, telegram_id, path="images"):
    files = os.listdir(path)
    bot = telegram.Bot(api)
    while True:
        try:
            random.shuffle(files)
            for file in files:
                with open(os.path.join(path, file), "rb") as photo:
                    bot.send_photo(telegram_id, photo=photo)
                    sleep(timer)
        except telegram.error.NetworkError:
            sleep(10)
            send_image(timer, api, telegram_id,  path)


def main():
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    images_path = os.getenv("IMAGES_PATH", default="images")
    os.makedirs("images", exist_ok=True)
    parser = argparse.ArgumentParser(description='Запускает бота')
    parser.add_argument(
        '--time',
        type=int, default=4,
        help="Время между отправки сообщение в часах",
    )
    time = parser.parse_args()
    send_image(time.time, telegram_token, telegram_chat_id, images_path)

if __name__ == "__main__":
    main()
