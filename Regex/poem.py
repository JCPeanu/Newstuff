import re #to use regular expressions
import random

#this block reads the words in english and puts them into a list
words_in_english = open("Popular.txt", "r")
all_words_list = list()
previous_word = " "
last_word_reached = False
while not last_word_reached:
    current_word = words_in_english.readline()
    current_word = current_word.rstrip("\n")
    if current_word == previous_word:
        last_word_reached = True
    else:
        all_words_list.append(current_word)
    previous_word = current_word
words_in_english.close()
 
#this block searches for a regular expression in that list
wrd1 = all_words_list[random.randint(0, len(all_words_list) - 1)]
while len(wrd1) < 4:
    wrd1 = all_words_list[random.randint(0, len(all_words_list) - 1)]
wrd2 = all_words_list[random.randint(0, len(all_words_list) - 1)]
while wrd2 == wrd1 and len(wrd2) < 4:
    wrd2 = all_words_list[random.randint(0, len(all_words_list - 1))]
def findRhyme(wrd1):
    lst = ["tion$", "all$", "wl$", "ace$", "ide$", "at$", "ip$", "and$", "oat$", "ill$", "ell$", "sion$", "en$", "ave$", "ay$", "ave$", "ump$", "ole$", "appy$", "ly$", "ness$", "ine$", "ero$", "ake$", "ing$", "ick$", "ow$", "ool$", "et$", "ive$", "eet$", "ee$", "oved$", "able$", "tal$"]
    x = re.search("tion$", wrd1)
    ind = 0
    while x == None:
        for i in range(len(lst)):
            x = re.search(lst[i], wrd1)
            if x != None:
                ind = i
                break
        if x == None:
            wrd1 = all_words_list[random.randint(0, len(all_words_list) - 1)]
            while len(wrd1) < 4:
                wrd1 = all_words_list[random.randint(0, len(all_words_list) - 1)]
    wrdlist = []
    for word in all_words_list:
        x = re.search(lst[ind], word)
        if (x!=None):
            wrdlist.append(word)
    ans = [wrdlist[random.randint(0, len(wrdlist) - 1)], wrd1]
    return ans
lst1 = findRhyme(wrd1)
lst2 = findRhyme(wrd2)
print(f"Some say that the world will end in {lst1[0]},\nSome say in {lst2[0]}.\nFrom what I've tasted of {lst1[1]}\nI hold with those who favor {lst1[0]}.\nBut if it had to be perish {lst2[1]},\nI think I know enough of hate\nTo know that for destruction {lst2[0]}\nIs also great,\nAnd would {lst2[1]}." )