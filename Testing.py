num = int(input("Please enter the height: "))
for i in range(1, num + 1):
    for j in range(i):
        print(",", end = "")
    print("\\", end = "")
    for j in range(2*(num - i)):
        print("-", end = "")
    print("/", end = "")
    for j in range (i):
        print(",", end = "")
    print()