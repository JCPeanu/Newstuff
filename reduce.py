from functools import reduce
# from math import lcm 
lst = [4, 2, 14, 7]
def lcm(a, b):
    for x in range(max(a, b), a*b + 1):
        if x % a == 0 and x % b == 0:
            return x
leastcm = reduce((lambda x, y : lcm(x, y)), lst)
print(leastcm)