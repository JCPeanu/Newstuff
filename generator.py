wrd = input("Please enter a phrase and I'm going to print each letter of it every time you press enter. Please enter the phrase: ")
def phrase_loop(word):
    word = word.split()
    pos = 0
    while(True):
        for words in word:
            yield words
            pos += 1
gen = phrase_loop(wrd)
while True:
    x = input()
    if x == "":
        print(next(gen), end = "")