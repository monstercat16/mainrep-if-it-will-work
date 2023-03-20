from random import randint

lst = [randint(0, 10) for i in range(10)]
print(*lst)
print(*set([i for index, i in enumerate(lst) if i in lst[index + 1:]]))
