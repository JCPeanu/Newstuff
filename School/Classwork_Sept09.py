x = (input("This program will display the literal representation of any positive four-digit number you input \nPlease input the number: "))
d1 = "zero"
d2 = "zero"
d3 = "zero"
d4 = "zero"
if (len(x) == 4):
    if(x[0] == "1"):
        d1 = "one"
    elif (x[0] == "2"):
        d1 = "two"
    elif (x[0] == "3"):
        d1 = "three"
    elif (x[0] == "4"):
        d1 = "four"
    elif (x[0] == "5"):
        d1 = "five"
    elif (x[0] == "6"):
        d1 = "six"
    elif (x[0] == "7"):
        d1 = "seven"
    elif (x[0] == "8"):
        d1 = "eight"
    elif (x[0] == "9"):
        d1 = "nine"

    if(x[1] == "1"):
        d2 = "one"
    elif (x[1] == "2"):
        d2 = "two"
    elif (x[1] == "3"):
        d2 = "three"
    elif (x[1] == "4"):
        d2 = "four"
    elif (x[1] == "5"):
        d2 = "five"
    elif (x[1] == "6"):
        d2 = "six"
    elif (x[1] == "7"):
        d2 = "seven"
    elif (x[1] == "8"):
        d2 = "eight"
    elif (x[1] == "9"):
        d2 = "nine"

    if(x[2] == "1"):
        d3 = "one"
    elif (x[2] == "2"):
        d3 = "two"
    elif (x[2] == "3"):
        d3 = "three"
    elif (x[2] == "4"):
        d3 = "four"
    elif (x[2] == "5"):
        d3 = "five"
    elif (x[2] == "6"):
        d3 = "six"
    elif (x[2] == "7"):
        d3 = "seven"
    elif (x[2] == "8"):
        d3 = "eight"
    elif (x[2] == "9"):
        d3 = "nine"

    if(x[3] == "1"):
        d4 = "-one"
    elif (x[3] == "2"):
        d4 = "-two"
    elif (x[3] == "3"):
        d4 = "-three"
    elif (x[3] == "4"):
        d4 = "-four"
    elif (x[3] == "5"):
        d4 = "-five"
    elif (x[3] == "6"):
        d4 = "-six"
    elif (x[3] == "7"):
        d4 = "-seven"
    elif (x[3] == "8"):
        d4 = "-eight"
    elif (x[3] == "9"):
        d4 = "-nine"
elif (len(x) == 3):
    print("check")
    if(x[0] == "1"):
        d2 = "one"
    elif (x[0] == "2"):
        d2 = "two"
    elif (x[0] == "3"):
        d2 = "three"
    elif (x[0] == "4"):
        d2 = "four"
    elif (x[0] == "5"):
        d2 = "five"
    elif (x[0] == "6"):
        d2 = "six"
    elif (x[0] == "7"):
        d2 = "seven"
    elif (x[0] == "8"):
        d2 = "eight"
    elif (x[0] == "9"):
        d2 = "nine"

    if(x[1] == "1"):
        d3 = "one"
    elif (x[1] == "2"):
        d3 = "two"
    elif (x[1] == "3"):
        d3 = "three"
    elif (x[1] == "4"):
        d3 = "four"
    elif (x[1] == "5"):
        d3 = "five"
    elif (x[1] == "6"):
        d3 = "six"
    elif (x[1] == "7"):
        d3 = "seven"
    elif (x[1] == "8"):
        d3 = "eight"
    elif (x[1] == "9"):
        d3 = "nine"

    if(x[2] == "1"):
        d4 = "-one"
    elif (x[2] == "2"):
        d4 = "-two"
    elif (x[2] == "3"):
        d4 = "-three"
    elif (x[2] == "4"):
        d4 = "-four"
    elif (x[2] == "5"):
        d4 = "-five"
    elif (x[2] == "6"):
        d4 = "-six"
    elif (x[2] == "7"):
        d4 = "-seven"
    elif (x[2] == "8"):
        d4 = "-eight"
    elif (x[2] == "9"):
        d4 = "-nine"
if (len(x) == 2):
    if(x[0] == "1"):
        d3 = "one"
    elif (x[0] == "2"):
        d3 = "two"
    elif (x[0] == "3"):
        d3 = "three"
    elif (x[0] == "4"):
        d3 = "four"
    elif (x[0] == "5"):
        d3 = "five"
    elif (x[0] == "6"):
        d3 = "six"
    elif (x[0] == "7"):
        d3 = "seven"
    elif (x[0] == "8"):
        d3 = "eight"
    elif (x[0] == "9"):
        d3 = "nine"

    if(x[1] == "1"):
        d4 = "-one"
    elif (x[1] == "2"):
        d4 = "-two"
    elif (x[1] == "3"):
        d4 = "-three"
    elif (x[1] == "4"):
        d4 = "-four"
    elif (x[1] == "5"):
        d4 = "-five"
    elif (x[1] == "6"):
        d4 = "-six"
    elif (x[1] == "7"):
        d4 = "-seven"
    elif (x[1] == "8"):
        d4 = "-eight"
    elif (x[1] == "9"):
        d4 = "-nine"
if (d3 == "one" and d4 == "-one"):
    d3 = ""
    d4 = "eleven"
elif (d3 == "one" and d4 == "-two"):
    d3 = ""
    d4 = "twelve"
elif (d3 == "one" and d4 == "-three"):
    d3 = ""
    d4 = "thirteen"
elif (d3 == "one" and d4 == "-four"):
    d3 = ""
    d4 = "fourteen"
elif (d3 == "one" and d4 == "-five"):
    d3 = ""
    d4 = "fifteen"
elif (d3 == "one" and d4 == "-six"):
    d3 = ""
    d4 = "sixteen"
elif (d3 == "one" and d4 == "-seven"):
    d3 = ""
    d4 = "seventeen"
elif (d3 == "one" and d4 == "-eight"):
    d3 = ""
    d4 = "eighteen"
elif (d3 == "one" and d4 == "-nine"):
    d3 = ""
    d4 = "nineteen"
print("The number {} in literal form is {}-thousand {}-hundred and {}{}".format(x, d1, d2, d3, d4))