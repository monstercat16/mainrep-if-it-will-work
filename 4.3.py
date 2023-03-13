def magictrick(dmy):
    d = dmy[:2]
    m = dmy[3:5]
    y = dmy[8:]
    if int(d) * int(m) == int(y):
        return True
    else:
        return False


date = input("dd.mm.yyyy: ")
print(magictrick(date))
