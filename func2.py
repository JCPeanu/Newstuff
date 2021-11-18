def pangrams(word):
    isP = True
    alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    word = word.lower()
    for x in word:
        alphabet[x] += 1
    lst = alphabet.values()
    for lst1 in lst:
        if (lst1 == 0):
            print("The phrase is a not pangram.")
            isP = False
            break
    if (isP):
        print("The phrase is a pangram.")


def palindromes(word):
    word = word.lower()
    new_word = ""
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]
    print("The phrase is a palindrome.") if (new_word == word) else print("The phrase is not a palindrome.")

x = input("Please enter a phrase and I will check if it is a pangram, containing every alphabet, and a palindrome, a sequence reading the same backword or forward. ")
x = "".join(x.split())
pangrams(x)
palindromes(x)
