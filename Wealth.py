import csv
import time
import random
with open("Wealth.csv", "r") as my_file:
    try:
        hasindicator = False
        Counter = 0
        Content = my_file.readlines()
        CoList = Content
        for i in CoList:
            if i:
                Counter += 1
        country = input("Which country would you like to see? ")
        print("Ok, wait... I have these indicators.")
        num_lst = []
        time.sleep(1)
        number = 1
        for i in range(1, Counter):
            split_string = CoList[i].split(",", 1)
            if split_string[0] == country.lower().capitalize():
                hasindicator = True
                num_lst.append(i)
                print(number, ". ", end = "", sep = "")
                try:
                    CoList[i].index("\"")
                    split_Str = CoList[i].split('\"')
                    print(split_Str[1])
                except:
                    split_string = CoList[i].split(",", 2)
                    print(split_string[1])
                number += 1
        if hasindicator:
            try:
                num = int(input("Which indictor would you like to know about? Please enter the number: "))
                lst = CoList[num_lst[num - 1]].split(",")
            except ValueError:
                num = int(input("Please enter a 'number': "))
            except:
                num = int(input("Please enter a 'number' within the range: "))
            if (num < len(num_lst)):
                lst = CoList[num_lst[num - 1]].split(",")
                new_lst = []
                actual_years = []
                years = [1995, 2000, 2005, 2010, 2014]
                for i in range(len(lst) - 5, len(lst)):
                    new_lst.append(lst[i].replace("\n", ""))
                print("The years such indicator was measured are: ", end = "")

                [actual_years.append(years[i]) for i in range(len(years)) if new_lst[i] != '' and new_lst[i] != '\n']
                if actual_years == []: 
                    print ("None.")
                else:
                    [print(i, " ",end = "") for i in actual_years]
                    print()
                    try:
                        year = int(input("Input the year you would like to check: "))
                    except:
                        print("Please enter a number.")
                        year = int(input("Input the year you would like to check: "))
                    try:
                        print("The value is: ", new_lst[actual_years.index(year)])
                    except:
                        print("No such year found.")
                        yr = random.randint(0, len(actual_years) - 1)
                        theyear = years.index(actual_years[yr])
                        print("Here's the value the indicator for another year:", new_lst[theyear], "in", actual_years[yr])
            else:
                print("Please enter the number within the range.")
        else:
            print("No such country found. Please run the program again.")
    except:
        print("An error has occured. Please run the program again.")
    else:
        print("Thanks for using my program.")
