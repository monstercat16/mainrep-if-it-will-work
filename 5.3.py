week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
x = int(input("how many off-time days you want? "))
weekend = week[0:x]
work = week[x:7]
print("weekend: ", *weekend)
print("work days: ", *work)
