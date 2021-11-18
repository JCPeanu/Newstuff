import random
lst = ["dog", "cat", "lizard", "fish", "hamster", "pig", "chick", "vacuum cleaner"]
x = lst.pop(random.randint(0, len(lst)))
y = lst.pop(random.randint(0, len(lst)))
print("Teacher, I'm so sorry for not submitting the homework on time, it was because my {} at my {}. Can I submit it later? \n Sent from my iPhone.".format(x, y))