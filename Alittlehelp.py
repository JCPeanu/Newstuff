import random

# introduce program
print("This program will return an anagram of the word entered.")

# user input
inputWord = str(input("Enter a word: "))

#The next code is going to place all the words in a set.
dictionary = open("/Users/joshuachen/Downloads/Mysite-master/Josh.txt", "r")
all_words = set()
previous_word = " "
Counter = 0
Findit = False
last_word_reached = False
while not last_word_reached:
        Counter += 1
        current_word = dictionary.readline()
        current_word = current_word.rstrip("\n")
        if current_word == previous_word:
            last_word_reached = True
        else:
            all_words.add(current_word)
        previous_word = current_word
dictionary.close()
all_words = list(all_words)
# all_words.remove(inputWord)

wrd_alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for wd in inputWord:
        wrd_alphabet[wd] += 1
while not Findit:
        new_wrd_alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        num = random.randint(0, Counter - 1)
        new_wrd = all_words[num].strip("\n")
        while abs(len(inputWord) - len(new_wrd)) >= 1:
            num = random.randint(0, Counter - 1)
            new_wrd = all_words[num].strip("\n")
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
