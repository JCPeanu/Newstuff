import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import csv
import time
import random

raw = pd.read_csv("Wealth.csv")

# with open("Wealth.csv", "r") as my_file:
#     try:
#         hasindicator = False
#         Counter = 0
#         Content = my_file.readlines()
#         CoList = Content
#         for i in CoList:
#             if i:
#                 Counter += 1
#         country = 'Albania'
#         num_lst = []
#         time.sleep(1)
#         number = 1
#         for i in range(1, Counter):
#             split_string = CoList[i].split(",", 1)
#             if split_string[0] == country.lower().capitalize():
#                 hasindicator = True
#                 num_lst.append(i)
#                 print(number, ". ", end = "", sep = "")
#                 try:
#                     CoList[i].index("\"")
#                     split_Str = CoList[i].split('\"')
#                     print(split_Str[1])
#                 except:
#                     split_string = CoList[i].split(",", 2)
#                     print(split_string[1])
#                 number += 1
#         if hasindicator:
#             try:
#                 num = int(input("Which indictor would you like to know about? I will use the data and create a graph for you. Please enter the number: "))
#                 lst = CoList[num_lst[num - 1]].split(",")
#             except ValueError:
#                 num = int(input("Please enter a 'number': "))
#             except:
#                 num = int(input("Please enter a 'number' within the range: "))
#         if (num <= len(num_lst)):
#             try:
#                 CoList[num].index("\"")
#                 split_Str = CoList[num].split('\"')
#                 indicator = split_Str[1]
#             except:
#                 split_string = CoList[num].split(",", 2)
#                 indicator = split_string[1]
#     except:
#         print("An error has occured. Please run the program again.")
list_of_indicators = raw["Indicator Name"].unique()
print("Please choose an indicator from this list: ")
for i in list_of_indicators:
    print(i)
indicator = input("Selected indicator: ")

print("You had chose '", indicator, "'. Thanks for using my code.", sep = "")
only_one_indicator = raw.loc[raw['Indicator Name'] == indicator]

modified_data = only_one_indicator.melt(id_vars=['Country Name'], value_vars = raw.columns[2:].values)

fig = px.line(modified_data, x = "variable", y = 'value', color = "Country Name", markers = True, title = indicator)
fig.show()