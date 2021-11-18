file1 = open("cattos.jpg", "rb").read()
x = bytearray(file1)
file2 = open("kitters.jpg", "rb").read()
y = bytearray(file2)
i = 0
leng = len(x)
while (i<leng):
    if (x[i] != y[i]):
        # print(x[i], " ", y[i])
        print(chr(x[i]), end = "")
        # chr(y[i]))
    i += 1
