import math
print("Welcome to Cylinder's volume and surface area calculator.\nI will use the height and base radius value enter by you to give you the result.")
h = float(input("Please enter the height: "))
br = float(input("Please enter the base radius: "))
v = (math.pi)*(br**2)*(h)
a = 2*(math.pi)*(br**2)+2*(math.pi)*(br)*(h)
print("The volume of the cylinder with the given values is {}m^3".format(format(v,'.2f')))
print("The area of the cylinder with the given values is {}m^2".format(format(a, '.2f')))
