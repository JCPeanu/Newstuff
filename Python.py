lst = [2, 4, 6, 9, 11]
Mine = lambda a : [lst[i] * a for i in range(len(lst))]
num = int(input("Please enter a number and I will print a list multiplied by that number and print it out: "))
print(Mine(num))
