def getNext(x):
    ans = x
    while(x > 0):
        ans += x%10
        x //= 10
    return ans

river1 = [1]
river3 = [3]
river9 = [9]
x = int(input("Please enter the river you would like to start with: "))
riveruser = []
riveruser.append(x)
def Digital_Rivers():
    isFalse = False
    ans1 = 0
    ans2 = 0
    ans3 = 0
    while(max(river1) < 15000):
        river1.append(getNext(river1[-1]))
    while(max(river3) < 15000):
        river3.append(getNext(river3[-1]))
    while max(river9) < 15000:
        river9.append(getNext(river9[-1]))
    while max(riveruser) < 15000:
        riveruser.append(getNext(riveruser[-1]))
    for j in riveruser:
        for l in river1:
            if j == l:
                f = int(j)
                stri= "river {} first meets river 1 at {}".format(x, f)
                return stri
    for j in riveruser:
        for l in river3:
            if j == l:
                f = int(j)
                stri= "river {} first meets river 3 at {}".format(x, f)
                return stri
    for j in riveruser:
        for l in river9:
            if j == l:
                f = int(j)
                stri= "river {} first meets river 9 at {}".format(x, f)
                return stri
print(Digital_Rivers())