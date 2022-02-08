print("Bisection method.")

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

lower_limit = -1000
#lower_limit_value = evaluate(lower_limit)
upper_limit = 1000
#upper_limit_value = evaluate(upper_limit)
midpoint = (lower_limit + upper_limit)/2
midpoint_value = evaluate(midpoint)

while abs(midpoint_value) > 0.0001:
    if midpoint_value > 0 and evaluate(upper_limit) > evaluate(lower_limit):
        upper_limit = midpoint
    elif midpoint_value > 0 and evaluate(upper_limit) < evaluate(lower_limit):
        lower_limit = midpoint
    elif midpoint_value < 0 and evaluate(upper_limit) > evaluate(lower_limit):
        lower_limit = midpoint
    else:
        upper_limit = midpoint
    midpoint = (lower_limit + upper_limit) / 2
    midpoint_value = evaluate(midpoint)
print("One root for the given equation is ", midpoint)