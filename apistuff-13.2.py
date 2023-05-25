import requests

# Запрашиваем у пользователя название города
city = input("Введите название города: ")

# Устанавливаем параметры для запроса
params = {
    "client_id": "RZW2IBXGEBOBCDDROC3WQB2YHMI14OM3QHFGRZAFVX5NFAEH",
    "client_secret": "O54ISCBMNM0KKSQ3SV2P2RM0FBB2K3LZDYLFFDMN2XQNOEJR",
    "v": "20230523",
    "near": city,
    "query": "достопримечательность",
    "limit": 10
}

# Отправляем GET-запрос к API Foursquare
response = requests.get("https://api.foursquare.com/v2/venues/search", params=params)

# Обрабатываем ответ и выводим две случайные достопримечательности
if response.ok:
    venues = response.json()["response"]["venues"]
    if len(venues) > 0:
        import random
        random_venues = random.sample(venues, min(len(venues), 2))
        for venue in random_venues:
            print(venue["name"])
    else:
        print("Для данного города не найдены достопримечательности")
else:
    print("Ошибка при выполнении запроса: %s (%s)" % (response.text, response.status_code))
