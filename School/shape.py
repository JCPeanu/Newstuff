print("I will use the two input, width and height, you gave me to print out a rectangle with the corresponding value length and height.")
w = int(input("Please enter the width: "))
h = int(input("Please enter the height: "))
for x in range(h):
    for y in range(w):
        print("* ", end="")
    print("")