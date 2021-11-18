print("I will used the inputed height to print out a triangle with the given height.")
h = int(input("Please enter the height: "))
if h == 1:
    print("/_\\")
else:
    for i in range(h - 1, 0, -1):
        for j in range(i):
            print(" ", end = "")
        print("/", end = "")
        for l in range((h - i - 1) * 2, 0, -1):
            print(" ", end = "")
        print("\\")
    print("/", end = "")
    for k in range(h*2-2):
        print("_", end = "")
    print("\\", end = "")
