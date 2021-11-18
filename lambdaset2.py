sets = {"hello there", "how are you"}
print("I'll print a set after all the spaces are removed. ")
x = input("Please enter a letter and I will remove every item of strings in a set that does not have a letter: ")
Mine = filter(lambda y : y.find(x) != -1, sets)
print(set(Mine))
