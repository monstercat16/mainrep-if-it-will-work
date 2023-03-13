def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)

    return sum


def luckyticket(number):
    edge = int(len(number) / 2)
    if int(len(number)) % 2 == 1:
        return print("ticket should have even amount of digits")
    else:
        a = getSum(int(number[:edge]))
        b = getSum(int(number[edge:]))
        if a == b:
            return print("lucky ticket!")
        else:
            return print("oh no, you didnt win")


ticket = input("your ticker number: ")
luckyticket(ticket)
