import json

with open('products.json', 'r') as file:
    data = json.load(file)

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии: Да")
    else:
        print("В наличии: Нет")
    print()