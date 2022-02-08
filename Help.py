import random
print("I will randomly select a palindrome from the text documents with over 350000 words.")
with open("Josh.txt", "r") as my_file:
    wrd = input().lower()
    Findit = False
    Counter = 0
    Content = my_file.readlines()
    CoList = Content
    wrd_alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for wd in wrd:
        wrd_alphabet[wd] += 1
    for i in CoList:
        if i:
            Counter += 1

    while not Findit:
        new_wrd_alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        num = random.randint(0, Counter - 1)
        new_wrd = Content[num].strip("\n")
        while abs(len(wrd) - len(new_wrd)) >= 1:
            num = random.randint(0, Counter - 1)
            new_wrd = Content[num].strip("\n")
        for wd in new_wrd:
            new_wrd_alphabet[wd] += 1
        wordlist = list(wrd_alphabet.keys())
        cnt = 0
        wrd_values = list(wrd_alphabet.values())
        new_wrd_values = list(new_wrd_alphabet.values())
        for i in range (26):
            if (cnt == 1):
                break
            if wrd_values[i] > new_wrd_values[i] and cnt < 1:
                cnt += 1
                for j in range(i, 26):
                    if wrd_values[j] < new_wrd_values[j]:
                        new_wrd_values[i] += 1
                        new_wrd_values[j] -= 1
                        letter2 = wordlist[j]
                        letter1 = wordlist[i]
                        break
            elif wrd_values[i] < new_wrd_values[i] and cnt < 1:
                cnt += 1
                for j in range(i, 26):
                    if wrd_values[j] > new_wrd_values[j]:
                        new_wrd_values[i] -= 1
                        new_wrd_values[j] += 1
                        letter2 = wordlist[i]
                        letter1 = wordlist[j]
                        break
        Findit = True
        for i in range (26):
            if wrd_values[i] != new_wrd_values[i]:
                Findit = False
                break
    print("The word is " + new_wrd + ", and the the change is by replacing " + letter1 + " with " + letter2 + ".")
        
        