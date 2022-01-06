# import random

# def randomgenerator():
#     return random.randint(0, 3) + 1

# x = int(input("Please enter the colums: "))
# y = int(input("Please enter the rows: "))
# people = [['_']*x]*y
# for i in range(x):
#     for j in range(y):
#         print(people[i][j]," ", end = "")
#     print()
# print()
# sum = x + y
# islessThan = True
# while (sum > 0):
#     if (sum > 3):
#         diff = random.randint(1, 3)
#         randx = random.randint(0, x - 1)
#         randy = random.randint(0, y - 1)
#         if (people[randx][randy] == '_'):
#             people[randx][randy] = diff
#         else:
#             while (people[randx][randy] == 3 or people[randx][randy] + diff > 3):
#                 randx = random.randint(0, x - 1)
#                 randy = random.randint(0, y - 1)
#             people[randx][randy] = diff
#             sum -= diff
#     elif (sum == 2):
#         diff = random.randint(1, 2)
#         randx = random.randint(0, x - 1)
#         randy = random.randint(0, y - 1)
#         if (people[randx][randy] == '_'):
#             people[randx][randy] = diff
#         else:
#             while (people[randx][randy] == 3 or people[randx][randy] + diff > 3):
#                 randx = random.randint(0, x - 1)
#                 randy = random.randint(0, y - 1)
#             people[randx][randy] = diff
#             sum -= diff
#     else:
#         randx = random.randint(0, x - 1)
#         randy = random.randint(0, y - 1)
#         if (people[randx][randy] == '_'):
#             people[randx][randy] = 1
#         else:
#             while (people[randx][randy] == 3 or people[randx][randy] + 1 > 3):
#                 randx = random.randint(0, x - 1)
#                 randy = random.randint(0, y - 1)
#             people[randx][randy] = 1
#             sum -= 1
# for i in range(x):
#     for j in range(y):
#         print(people[i][j]," ", end = "")
#     print()


# import random
# NotoverCrowded = True
# print("instructions")
# height = int(input("Enter the height: "))
# width = int(input("Enter the width: "))
# x = 0
# num = height + width
# num_list = []
# while sum(num_list)<num:
#    if num - sum(num_list) >= 3:
#        y = random.randint(1, 3)
#        num_list.append(y)
#    elif num - sum(num_list) == 2:
#        y = random.randint(1, 2)
#        num_list.append(y)
#    elif num - sum(num_list) == 1:
#        y = 1
#        num_list.append(y)
# print(num_list)

# location_list = []
# dict = {}
# for i in range(0,len(num_list)):
#     key = num_list[i]
#     x = random.randint(1, width)
#     y = random.randint(1, height)
#     location = (x,y)
#     while location in location_list:
#         x = random.randint(1, width)
#         y = random.randint(1, height)
#         location = (x, y)
#     location_list.append(location)
#     dict[f'{location}'] = f'{key}'

# print(dict)

# for j in range(1, height + 1):
#    line = ''
#    for i in range(1, int(width) + 1):
#        location = (i,j)
#        if f'{location}' in dict.keys():
#            number = dict.get(f'{location}')
#            value = f'{number} '
#        else:
#            value = '_ '
#        line = line+value
#    print(f'{line}')
# print()

# population = dict.values()
# x = random.randint(1, width)
# y = random.randint(1, height)
# location = (x, y)
# if location in location_list:
#     popu = int(dict[f'{location}'])
#     del dict[f'{location}']
#     popu += 1
#     dict[f'{location}'] = f'{popu}'
# else:
#     dict[f'{location}'] = 1
#     location_list.append(location)
# print(dict)

# while NotoverCrowded:
#     if '4' in population:
#         NotoverCrowded = False
#     else:
#         x = random.randint(1, width)
#         y = random.randint(1, height)
#         location = (x, y)
#         if location in location_list:
#             popu = int(dict[f'{location}'])
#             del dict[f'{location}']
#             popu += 1
#             dict[f'{location}'] = f'{popu}'
#         else:
#             dict[f'{location}'] = 1
#             location_list.append(location)
#         for j in range(1, height + 1):
#             line = ''
#             for i in range(1, width + 1):
#                 location = (i,j)
#                 if f'{location}' in dict.keys():
#                     number = dict.get(f'{location}')
#                     value = f'{number} '
#                 else:
#                     value = '_ '
#                     line += value
#             print(f'{line}')
#         print()

import random
import time
NotoverCrowded = True
allhave = False
print("This code simulates migration. Enter the dimensions for your population grid.")
height = int(input("Enter the height: "))
width = int(input("Enter the width: "))
x = 0
num = height + width
num_list = []

# generating the original grid
while sum(num_list) < num:
   if num - sum(num_list) >= 3:
       y = random.randint(1, 3)
       num_list.append(y)
   elif num - sum(num_list) == 2:
       y = random.randint(1, 2)
       num_list.append(y)
   elif num - sum(num_list) == 1:
       y = 1
       num_list.append(y)
print(num_list)

location_list = []
dict = {}
for i in range(0,len(num_list)):
   key = num_list[i]
   x = random.randint(1, width)
   y = random.randint(1, height)
   location = (x,y)
   dict[f'{location}'] = f'{key}'
   if location in location_list:
       # x = random.randint(1,
       pass
   # while location not in location_list:
   else:
       location_list.append(location)
       dict[f'{location}'] = f'{key}'
print(location_list)
print(dict)

for j in range(int(height),0,-1):
   line = ''
   for i in range(1, int(width) + 1):
       location = (i,j)
       if f'{location}' in dict.keys():
           number = dict.get(f'{location}')
           value = f'{number} '
       else:
           value = '_ '
       line = line + value
   print(f'{line}')
print()

population = dict.values()
while not allhave:
    if '4' in population:
        if '1' in population or '' in population or '0' in population:
            allhave = False
        else:
            allhave = True
            break
        values = list(dict.values())
        coordinates = list(dict.keys())
        NotoverCrowded = False
        position = values.index('4')
        location = coordinates[position]
        x = int(location[1])
        y = int(location[4])
        location1 = (x-1,y)
        location2 = (x+1,y)
        location3 = (x,y-1)
        location4 = (x,y+1)
        if x - 1 >= 1:
            if location1 not in location_list:
                d = {f'{location1}': '1'}
                dict.update(d)
                location_list.append(location1)
                oldpopu = int(dict.get(f'{location}'))
                oldpopu -= 1
                old_d = {f'{location}': f'{oldpopu}'}
                dict.update(old_d)
            else: 
                popu = int(dict.get(f'{location1}'))
                if (popu <= 3):
                    popu += 1
                    d = {f'{location1}': f'{popu}'}
                    dict.update(d)
                    oldpopu = int(dict.get(f'{location}'))
                    oldpopu -= 1
                    old_d = {f'{location}': f'{oldpopu}'}
                    dict.update(old_d)
            coordinates = list(dict.keys())
            values = list(dict.values())
        if x + 1 <= width:
            if location2 not in location_list:
                d = {f'{location2}': '1'}
                dict.update(d)
                location_list.append(location2)
                oldpopu = int(dict.get(f'{location}'))
                oldpopu -= 1
                old_d = {f'{location}': f'{oldpopu}'}
                dict.update(old_d)
            else:
                popu = int(dict.get(f'{location2}'))
                if (popu <= 3):
                    popu += 1
                    d = {f'{location2}': f'{popu}'}
                    dict.update(d)
                    oldpopu = int(dict.get(f'{location}'))
                    oldpopu -= 1
                    old_d = {f'{location}': f'{oldpopu}'}
                    dict.update(old_d)
            coordinates = list(dict.keys())
            values = list(dict.values())
        if y - 1 >= 1:
            if location3 not in location_list:
                d = {f'{location3}': '1'}
                dict.update(d)
                location_list.append(location3)
                oldpopu = int(dict.get(f'{location}'))
                oldpopu -= 1
                old_d = {f'{location}': f'{oldpopu}'}
                dict.update(old_d)
            else:
                popu = int(dict.get(f'{location3}'))
                if (popu <= 3):
                    popu += 1
                    d = {f'{location3}': f'{popu}'}
                    dict.update(d)
                    oldpopu = int(dict.get(f'{location}'))
                    oldpopu -= 1
                    old_d = {f'{location}': f'{oldpopu}'}
                    dict.update(old_d)
            coordinates = list(dict.keys())
            values = list(dict.values())
        if y + 1 <= height:
            if location4 not in location_list:
                d = {f'{location4}': '1'}
                dict.update(d)
                location_list.append(location4)
                oldpopu = int(dict.get(f'{location}'))
                oldpopu -= 1
                old_d = {f'{location}': f'{oldpopu}'}
                dict.update(old_d)
            else:
                popu = int(dict.get(f'{location4}'))
                if (popu <= 3):
                    popu += 1
                    d = {f'{location4}': f'{popu}'}
                    dict.update(d)
                    oldpopu = int(dict.get(f'{location}'))
                    oldpopu -= 1
                    old_d = {f'{location}': f'{oldpopu}'}
                    dict.update(old_d)
            coordinates = list(dict.keys())
            values = list(dict.values())
        population = dict.values()
        if '4' not in values:
            NotoverCrowded = True
        if '1' in values or '' in values or '0' in values:
            allhave = False
        else:
            allhave = True
        for j in range(height, 0, -1):
            line = ''
            for i in range(1, int(width) + 1):
                location = (i,j)
                if f'{location}' in dict.keys():
                    number = dict.get(f'{location}')
                    if number == '0':
                        value = '_ '
                    else:
                        value = f'{number} '
                else:
                    value = '_ '
                line = line + value
            print(f'{line}')
        print('')
    else:
        x = random.randint(1, width)
        y = random.randint(1, height)
        location = (x,y)
 
        if location in location_list:
            popu = int(dict.get(f'{location}'))
            popu += 1
            d = {f'{location}': f'{popu}'}
            dict.update(d)
        else:
            d = {f'{location}': '1'}
            dict.update(d)
            location_list.append(location)
        if '1' or '' or '0' in population:
            allhave = False
        else:
            allhave = True
        if '4' in population:
            NotoverCrowded = True
        for j in range(height, 0, -1):
            line = ''
            for i in range(1, int(width) + 1):
                location = (i,j)
                if f'{location}' in dict.keys():
                    number = dict.get(f'{location}')
                    if number == '0':
                        value = '_ '
                    else:
                        value = f'{number} '
                else:
                    value = '_ '
                line = line + value
            print(f'{line}')
        print('')
    time.sleep(1)
print("This is the end of the migration.")