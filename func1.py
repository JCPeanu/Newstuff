num = int(input("Please enter a number and I will call the collatz function until it returns 1. "))
def collatz(number):
    if (number%2==0):
        print(number//2, end = " ")
        number = number//2
    else:
        print(number*3+1, end = " ")
        number = number*3+1
    return number
while (num!= 1):
    num = collatz(num)