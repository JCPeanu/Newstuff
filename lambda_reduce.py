from functools import reduce
lst = [4, 2, 14, 7]
lst.sort()
def lcm():
    num = reduce(lambda x, y : x * y, lst)
    for i in range(lst[-1], num + 1, lst[-1]):
        is_LCM = True
        for j in lst:
            if i % j != 0:
                is_LCM = False
                break
        if (is_LCM):
            print(i)
            break
print("I will print the product of all the values in the list.")
print(lst)
lcm()