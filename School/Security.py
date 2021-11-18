import random
str = input("Please enter a word: ")
lst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
neww = ""
str = str.upper()
for token in str:
    for i in range(len(lst)):
        if token == lst[i]:
            num = random.randint(0,25)
            neww += lst[(i + 1 +num)%26]
print(neww)
ans = ""
for j in range(25):
    for l in range(25):
        for k in range(25):
            for m in range(25):
                for n in range (25):
                    ans = lst[j] + lst[l] + lst[k] + lst[m] + lst[n]
                    if (ans == str):
                        print(f"The answer is {ans}.")
                        break