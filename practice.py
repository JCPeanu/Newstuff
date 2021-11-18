word = "python"
x = 5
l = 2
for i in range(1, 6):
    for j in range(0, i):
        print(word[x%6] + " ", end = "")
        x += l
        l -= 2
        if l == 0: l = 2
    x = 5 - i%6
    print("")
    l = 0