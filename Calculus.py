print("Calculus Calculator.")

print("Please enter the function you want to solve.")
degree = int(input("Which degree is your function? "))

coefficients = list()
for i in range(degree + 1):
    constant = float(input(f"Please enter the coefficient of x^{degree-i} "))
    coefficients.append(constant)

print("The equation to solve is ")
for i in range(0, degree + 1):
    print(f"({coefficients[i]}x^{degree - i}) + ", end = "")
print(f"({coefficients[degree]})")

def evaluate(point):
    result  = 0
    for i in range(degree + 1):
        result += coefficients[i]*pow(point, (degree - i))
    return result

lower_limit = float(input("Which value of x is the lower limit? "))
upper_limit = float(input("Which value of x is the upper limit? "))

dx = 0.0001

area = 0
x = lower_limit
while x < upper_limit:
    area += (evaluate(x) * dx)
    x += dx

print(f"The rae of the function given between {lower_limit} and {upper_limit} is {area} square units. ")