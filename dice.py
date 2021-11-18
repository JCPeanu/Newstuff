import random
def dice_roller(sides):
    if sides[0] == '':
        print(random.randint(1, 20))
    else:
        for side in sides:
            print(random.randint(1, int(side)))
print("You enter the number of sides a dice has and the number of times you would like to roll, and I would give you the result of each roll.")
num = []
num = list(input("Please enter the number of sides each dice has: ").split(', '))
dice_roller(num)