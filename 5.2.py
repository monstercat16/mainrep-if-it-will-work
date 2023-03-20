numbers = [1, 2, 3, 4, 5]
if len(set(numbers)) != len(numbers):
    print("В списке есть повторяющиеся элементы")
    for number in set(numbers):
        if numbers.count(number) > 1:
            print(number)
else:
    print("В списке нет повторяющихся элементов")