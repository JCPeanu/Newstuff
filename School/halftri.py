print("I will used the inputed height to print out a right triangle with the given height.")
h = int(input("Please enter the height: "))
for i in range(0, h - 1):
    print("|", end = "")
    for j in range(0, i):
        print(" ", end = "")
    print("\\")
print("|", end = "")
for l in range(0, h-1):
    print("_", end = "")
print("\\")
