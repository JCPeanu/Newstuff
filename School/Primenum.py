print(2, end = " ")
x = 3
while (x < 100):
    isPrime = True
    for i in range(2, x):
        if (x % i == 0):
            isPrime = False
            break
    if (isPrime == True):
        print(x, end = " ")
    x += 1
    