print("I will used the inputed height to print out a diamond shape with the given height.")
h = int(input("Please enter an even value height: "))
while (h % 2 != 0):
    h = int(input("Please enter an even value height: "))
h /= 2
h = int(h)
for i in range(h, 0, -1):
    for j in range(i):
        print(" ", end = "")
    print("/", end = "")
    for l in range((h - i) * 2, 0, -1):
        print(" ", end = "")
    print("\\")
for k in range(h):
    for m in range(k + 1):
        print(" ", end = "")
    print("\\", end = "")
    for n in range((h - k - 1) * 2, 0, -1):
        print(" ", end = "")
    print("/")
    