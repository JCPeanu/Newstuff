# # l = 2
# # x = 3
# # lst = [2]
# # while (x < 1000):
# #     opsum = ""
# #     isPrime = True
# #     for i in range(2, x):
# #         if (x % i == 0):
# #             isPrime = False
# #             break
# #     if (isPrime == True):
# #         lst.append(x)
# #     x += 1

# # for i in range(len(lst)):
# #     num1 = str(lst[i])
# #     num2 = num1[::-1]
# #     print(num2)
# #     for j in range(len(lst)):
# #         if (num2 != lst[j]):
# #             lst.pop(i)
# # print(lst)

# word = input("Plase enter a word: ")
# h = int(input("Please enter a height: "))
# x = -1
# for i in range(h, 0, -1):
#     for j in range(h + 1 - i):
#         print(word[x%len(word)], end = " ")
#         x -= 1
#     print()