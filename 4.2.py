def task(x):
    x = str(x)
    if x.isdigit():
        # integer
        if int(x) == 0:
            return (print("ZeroDivisionError"))
        else:
            return (print(100 // int(x)))
    else:
        # string
        return (print("ValueError"))


q = input("smth: ")
task(q)
