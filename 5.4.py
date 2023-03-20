list1 = ['Иванов', 'Петров', 'Сидоров', 'Смирнов', 'Кузнецов', 'Дмитриев', 'Морозов', 'Новиков', 'Федоров', 'Попов']
list2 = ['Козлов', 'Макаров', 'Кириллов', 'Егоров', 'Гришин', 'Степанов', 'Тимофеев', 'Яковлев', 'Никитин', 'Гусев']

team = (list1[0], list1[2], list1[4], list1[6], list1[8], list2[1], list2[3], list2[5], list2[7], list2[9])

print("Исходные списки:")
print("Группа 1:", list1)
print("Группа 2:", list2)
print("Спортивная команда:", team)

print("Длина кортежа:", len(team))

team_sorted = sorted(team)
print("Отсортированный кортеж:", team_sorted)

if "Иванов" in team:
    print("Студент Иванов входит в команду")
    print("Количество фамилий Иванов в команде:", team.count("Иванов"))
else:
    print("Студент Иванов не входит в команду")

