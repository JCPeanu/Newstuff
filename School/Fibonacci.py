x = int(input("I will print the Fibonacci sequence less than or equal the number you entered.\nPlease enter a number: "))
a = 1
b = 1
c = 0
while (a <= x):
    print (a, " ", end = "", sep=",")
    c = a
    a = b
    b = a + c
print("\b\b.")
print("Thank you for using this code.")
