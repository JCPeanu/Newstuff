print("I'll print a diamond!")

h = int(input("How many lines should it span? Please enter an even number: "))

if (h % 2 != 0):
    h = int(input("How many lines should it span? Please enter an even number: "))

half = int(h/2)
x = 1
for i in range(half):
    for n in range(half - i):
        print(" ", end = "")
    for j in range(i + 1):
        print("/", end = "")
    for l in range(i + 1):
        print("\\", end = "")
    print()
for m in range(half, 0, -1):
    for n in range(half - m + 1):
        print(" ", end = "")
    for j in range(m):
        print("\\", end = "")
    for l in range(m):
        print("/", end = "")
    print()