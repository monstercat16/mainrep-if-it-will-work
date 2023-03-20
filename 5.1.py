numbers = (1, 2, 3, 4, 5)
x = int(input("enter number: "))
if x in numbers:
    print(numbers)
    print(x)
    print("congrats, you guessed right number ")
else:
    print(numbers)
    print(x)
    print("unknown number ")
