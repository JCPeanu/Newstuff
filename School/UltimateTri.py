h = int(input("Please enter the height of a pyramid: "))
th = 3*h
x = 0
for i in range(th - 1, 0, -3):
    x = i
    for v in range(0, 3*2, 2):
        for f in range(x):
            print (" ", end = "")
        x -= 1
        print("/", end = "")
        for c in range(v):
            print(" ", end = "")
        print("\\")