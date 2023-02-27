x = input("Input first color: ")
x1 = input("Input second color: ")
z1= "red"
z2= "blue"
z3= "yellow"
if (x == z1) and (x1 == z2):
    print("purple")
elif (x == z1) and (x1 == z3):
    print("orange")
elif (x == z2) and (x1 == z3):
    print("green")
elif (x1 == z1) and (x == z2):
    print("purple")
elif (x1 == z1) and (x == z3):
    print("orange")
elif (x1 == z2) and (x == z3):
    print("green")
else:
    print("Error")