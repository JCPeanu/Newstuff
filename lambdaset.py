sets = {"hello there", "how are you"}
print("I'll print a set after all the spaces are removed. ")
Mine = map(lambda x : x.replace(" ", ""), sets)
print(set(Mine))
