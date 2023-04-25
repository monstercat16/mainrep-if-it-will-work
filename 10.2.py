import json

with open('products.json', 'r') as file:
    data = json.load(file)

new_product = {}
new_product['name'] = input('Введите название продукта: ')
new_product['price'] = int(input('Введите цену продукта: '))
new_product['available'] = True if input('Товар в наличии? (y/n) ').lower() == 'y' else False
new_product['weight'] = int(input('Введите вес продукта: '))
data['products'].append(new_product)

with open('products.json', 'w') as file:
    json.dump(data, file, indent=4)

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии: Да")
    else:
        print("В наличии: Нет")
    print()
