x = int(input("Please enter a number:"))
i = 2
if (x % i == 0):
    print(i)
i += 1
while (i < x):
    isPrime = True
    if (x % i == 0):
        # if x is divisiable by i
        for j in range(2, i):
            if (i % j == 0):
                isPrime = False
        if isPrime == True:
            print(i)
    i += 1