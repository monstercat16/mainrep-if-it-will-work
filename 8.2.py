from PIL import Image
cards = {
    'День рождения': 'birthday_card.jpg',
    'Новый год': 'new_year_card.jpg',
    '8 Марта': 'womens_day_card.jpg'
}

holiday = input('Какой праздник Вас интересует? ')

if holiday in cards:
    card_file = cards[holiday]
    card_image = Image.open(card_file)
    card_image.show()
else:
    print('Извините, открытки для этого праздника нет')