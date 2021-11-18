import random
x = random.randint(0, 100)
ans = input("Please guess a number between 0 and 100 ")
while (int(ans) != int(x)):
    if int(ans) > x:
        print("The number is too large")
    else:
        print("The number is too small")
    ans = input()
print("Great! You got the number!")