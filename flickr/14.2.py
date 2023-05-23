# https://api.flickr.com/services

# a41956e04d7c0581697c214c254631b5 - key

# bcc487c0ad6e9070 - secret

import webbrowser
import requests

# Замените "YOUR_API_KEY" на ваш ключ API Flickr
api_key = "a41956e04d7c0581697c214c254631b5"

# Запрос информации о пользователе по username
username = input("Введите имя пользователя на Flickr: ")
url = f"https://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key={api_key}&username={username}&format=json&nojsoncallback=1"
response = requests.get(url)
data = response.json()

# Получение ID пользователя
user_id = data["user"]["id"]

# Открытие профиля пользователя в браузере
webbrowser.open(f"https://www.flickr.com/people/{user_id}/")
