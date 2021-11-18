x = 4
i = 1
while (i <= 100):
    for j in range(2, x):
        if (x % j != 0):
            i += 1
            break
    x += 1
print (x)