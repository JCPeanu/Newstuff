def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

def integer_digits(x):
    if (x <= 0.00001):
        wrd = str(x)
        return int(wrd[-1])
    else:
        return len(str(x)) - 2

def Euler_Number(threshold = 0.00001, paused = False):
    ans = 0.0
    i = 0
    j = 1
    trueans = 1.0
    digits = integer_digits(threshold)
    if (paused == True):
        while (trueans - ans > threshold):
            trueans += (1/factorial(j))
            ans += (1/factorial(i))
            if (input() == ''):
                print(round(ans, digits), end = '')
            i += 1
            j += 1
        return ''
    while (trueans - ans > threshold):
        ans += (1/factorial(i))
        trueans += (1/factorial(j))
        i += 1
        j += 1
    return round(ans, digits)
print(Euler_Number(paused = True))
print(Euler_Number(0.01))
print(Euler_Number(0.1, True))