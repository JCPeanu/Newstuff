print("Tangent Calculator.")

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

point = float(input("At whcih point do you want to find the derivative? "))

lower_point = point - 0.00001
upper_point = point + 0.00001

lower_point_value = evaluate(lower_point)
upper_point_value = evaluate(upper_point)

slope = (upper_point_value - lower_point_value)/(upper_point - lower_point)

print("The answer is ", slope)