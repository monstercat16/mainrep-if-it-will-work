smth = [1, 1, 2, 3, 1, 3, 3, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
l = len(smth)
s = ""
# for i in range(1, l):
#    if smth[i - 1] == smth[i]:
#        while True:
#
#       s += str(smth[i - 1]) + str(smth[i]) + " "
for i in range(l-1):
    n = 1
    c = 0
    while smth[i] == smth[i + n]:
        n += 1
        c += 1
    s += str(smth[i]) * c

if s != "":
    print("there is duplicates: ")
    print(s)
