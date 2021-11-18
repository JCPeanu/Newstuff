import random
opts = ["Rock", "Paper", "Scissors"]
y = input("How many times do you want to play?")
for j in range(int(y)):
    x = input("Rock--Paper--Scissors! ")
    num = random.randint(0,2)
    while(x == opts[num]):
        print(x, "vs.", opts[num])
        print("Tie")
        x = input()
        num = random.randint(0,2)
    print(x, "vs.", opts[num])
    if x == opts[0]:
        if opts[num] == opts[2]:
            print("You've won!")
        else:
            print("You've lost!")
    if x == opts[1]:
        if opts[num] == opts[0]:
            print("You've won!")
        else:
            print("You've lost!")
    if x == opts[2]:
        if opts[num] == opts[1]:
            print("You've won!")
        else:
            print("You've lost!")
    if (x != opts[0] or x != opts[1] or x != opts[2]):
        print("Please enter the correct input.")