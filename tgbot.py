import argparse
import random
import sys
import telegram
import os
from dotenv import load_dotenv
from time import sleep

def send_image(timer, api, id):
    files = os.listdir("images")
    bot = telegram.Bot(api)
    random.shuffle(files)
    for file in files:
        with open(f"images\{file}", "rb") as photo:
            bot.send_photo(id, photo=photo)
            sleep(timer * 3600)



def main():
    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    parser = argparse.ArgumentParser(description='Запускает бота')
    parser.add_argument('--time', type=int, default=4, help="Время между отправки сообщение в часах")
    time = parser.parse_args()
    send_image(time.time, telegram_token, telegram_chat_id)

if __name__ == "__main__":
    main()