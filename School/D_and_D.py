import random
lst = []
print (random.random())
lst.append(random.randint(1, 20))
# print("Two 20-sided dice are thrown: {}, {}".format(lst[0], lst[1]))
# if (lst[0] >= lst[1]):
#     print("If you have an advantage roll the result would be {}.".format(lst[0]), end = "")
#     if (lst[0] == 20):
#         print(" Critical Hit!")
#     else:
#         print()
#     print("if that's a disadvantage roll you'd got a {}.".format(lst[1]),end = "")
#     if (lst[1] == 1):
#         print("Critical Miss!")
# else:
#     print("If you have an advantage roll the result would be {}".format(lst[1]))
#     if (lst[1] == 20):
#         print(" Critical Hit!")
#     else:
#         print()
#     print("if that's a disadvantage roll you'd got a {}.".format(lst[1]),end = "")
#     if (lst[0] == 1):
#         print("Critical Miss!")