x = int(input("Which number do you want to print the multiplication table of? "))
y = int(input("Until which value do you want to print the multiplication table? "))
print("Here is the multiplication table for {} until {}:".format(x, y))
z = 1
while (z <= y):
    print("{} x {} = {}".format(x, z, x*z))
    z += 1