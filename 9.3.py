import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # пропускаем первую строку с названиями столбцов
    total_cost = 0
    products = []
    for row in reader:
        product, quantity, price = row
        cost = int(quantity) * int(price)
        products.append(f'{product} - {quantity} шт. за {price} руб.')
        total_cost += cost

print('Нужно купить:')
print('\n'.join(products))
print(f'Итоговая сумма: {total_cost} руб.')