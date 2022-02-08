import random
print("I will randomly select a palindrome from the text documents with over 350000 words.")
with open("Josh.txt", "r") as my_file:
    Counter = 0
    Content = my_file.readlines()
    CoList = Content

    for i in CoList:
        if i:
            Counter += 1
    num = random.randint(1, Counter-1)
    wrd = Content[num].strip("\n")
    new_wrd = ""
    for i in range (len(wrd)-1, -1, -1):
            new_wrd += wrd[i]
    if wrd == new_wrd:
        print(wrd)
    else:
        while wrd != new_wrd:
            num = random.randint(1, Counter-1)
            wrd = Content[num].strip("\n")
            new_wrd = ""
            for i in range (len(wrd)-1, -1, -1):
                new_wrd += wrd[i]
            if wrd == new_wrd:
                print(wrd)
