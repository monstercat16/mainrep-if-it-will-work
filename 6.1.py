dict = {"Россия": "Москва", "США": "Вашингтон", "Франция": "Париж", "Германия": "Берлин"}

for key, value in dict.items():
    print(key, "-", value)

country = input("Введите название страны: ")
if country in dict:
    print("Столица", country, "-", dict[country])
else:
    print("Такой страны нет в списке")

sdict = sorted(dict.items())
for key, value in sdict:
    print(key, "-", value)
