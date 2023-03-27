week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
x = int(input("how many off-time days you want? "))
y =7-x
weekend = week[y:7]
work = week[0:y]
print("weekend: ", *weekend)
print("work days: ", *work)
