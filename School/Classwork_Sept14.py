# lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day = input("What is today's date? ")
# day2 = input("What is the future date? ")
# x = 0
# y = 0
# for i in range(6):
#     if (lst[i] == day):
#         x = i + 1
#     elif (lst[i] == day2):
#         y = i + 1
# if (y < x):
#     y = (7-x) + y
#     print(y)
# else:
#     print(y-x)

day = input("What is today's date? ")
day2 = input("What is the future date? ")
x = 0
y = 0
if (day == "Monday"):
    x = 1
elif (day == "Tuesday"):
    x = 2
elif (day == "Wednesday"):
    x = 3
elif (day == "Thursday"):
    x = 4
elif (day == "Friday"):
    x = 5
elif (day == "Saturday"):
    x = 6
elif (day == "Sunday"):
    y = 7

if (day2 == "Monday"):
    y = 1
elif (day2 == "Tuesday"):
    y = 2
elif (day2 == "Wednesday"):
    y = 3
elif (day2 == "Thursday"):
    y = 4
elif (day2 == "Friday"):
    y = 5
elif (day2 == "Saturday"):
    y = 6
elif (day2 == "Sunday"):
    y = 7

if (y < x):
    y = (7-x) + y
    print("You have to wait {} more days.".format(y))
else:
    print("You have to wait {} more days.".format(y-x))