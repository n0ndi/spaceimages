# Скачивание изображений космоса

Скачивает изображение космоса с API NASA и сайта SpaceXData.Так же отправляет их в Telegram чаты.

### Как установить

<p>Для работы программы требуется API ключ (nasa.gov), создайте API ключ (nasa.gov) и запишите его в в файле .env (NASA_TOKEN=ваш ключ).
Вот как он выглядит:</p> 63BIffdb6d247MTCafejCPtEuioP9zxOtD5NC.
<p>Так же нужен API телеграм бота созданного в Bot Father и ID канала в телеграме.Их так же нужно записать в .env файл: <p>(TELEGRAM_TOKEN=Ваш api бота)<p>(TELEGRAM_CHAT_ID=Ваш id чата)</p>
<p>Можно настроить директорию фотографий, через настройку в .env (IMAGES_PATH=Ваша директория)</p>
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
### Возможности скриптов
<p>apod_nasa_images.py - --count COUNT - скачивает фотографии дня с сайта NASA(COUNT по умолчанию 20 )<p>
<p>epic_nasa_images.py - скачивает фотографии земли с сайта NASA<p>
<p>fetch_spacex_launch.py --launch_id LAUNCH_ID - скачивает фотографии запуска с SpaceX(LAUNCH_ID по умолчанию последний запуск)<p>
<p>tgbot.py --time TIME - запускает бота выкладывающий фото через определённое время(TIME по умолчанию 4 часа)<p>

### Пример запуска скриптов
```
apod_nasa_images.py
```
```
apod_nasa_images.py --count 10
```
```
epic_nasa_images.py
```
```
fetch_spacex_launch.py
```
```
fetch_spacex_launch.py --launch_id 5eb87d47ffd86e000604b38a
```
```
tgbot.py
```
```
tgbot.py --time 2
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

