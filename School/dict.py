str = input("Tell me something and I'll count its letters: ").lower()

dict = dict()
for elements in str:
    if (elements not in dict.keys() and elements != " "):
        dict.setdefault(elements, 1)
    elif(elements != " "):
        dict[elements] = dict[elements] + 1
lst1 = list(dict.keys())
lst2 = list(dict.values())
[print(lst2[i], lst1[i]) if (lst2[i] == 1) else print(lst2[i], lst1[1], "'s") for i in range(len(lst1))]