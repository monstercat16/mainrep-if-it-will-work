num = int(input("num of words: "))
line = ""
linefinal = ""
for i in range(num):
    line = input("input word: ")
    linefinal += line + " "
print(linefinal)
