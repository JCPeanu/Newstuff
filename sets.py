print("This program will classify actors present in movies for you, and enter break will end the input.")
set1 = set({})
set2 = set({})
set3 = set({})
name1 = input('Please input the actors and actresses present in "How my hamster ate my vacuum cleaner": ')
print(name1)
print(name1.split(", "))
set1 = set(name1.split(", "))
name2 = input('Please input the actors and actresses present in "Fractal restaurant": ')
set2 = set(name2.split(", "))
name3 = input('Please input the actors and actresses present in "Kristopher\'s Bizarre Adventure": ')
set3 = set(name3.split(", "))
print("The actors present in all movies are: ", end = "")
print(",".join(set1 & set2 & set3)) if ",".join(set1 & set2 & set3) != "" else print("None")
print('The actors present in "How my hamster ate my vacuum cleaner" and "Fractal restaurant" only are: ', end = "")
[print(",".join((set1 & set2) - set3)) if ",".join((set1 & set2) - set3) != "" else print("None")]
print('The actors present in "How my hamster ate my vacuum cleaner" and "Kristopher\'s Bizarre Adventure" only are: ', end = "")
[print(",".join(set1 & set3 - set2)) if ",".join(set1 & set3 - set2) != "" else print("None")]
print(f'The actors present in "Kristopher\'s Bizarre Adventure" and "Fractal restaurant" only are: ', end = "")
[print(",".join(set2 & set3 - set1)) if ",".join(set2 & set3 - set1) != "" else print("None")]
print(f'The actors present only in "How my hamster ate my vacuum cleaner" are: ', end = "")
[print(",".join(set1 - (set2 | set3))) if ",".join(set1 - (set2 | set3)) != "" else print("None")]
print(f'The actors present only in "Fractal restaurant" are: ', end = "")
[print(",".join(set2 - (set1 | set3))) if ",".join(set2 - (set1 | set3)) != "" else print("None")]
print(f'The actors present only in "Kristopher\'s Bizarre Adventure" are: ', end = "")
[print(",".join(set3 - (set1 | set2))) if ",".join(set3 - (set1 | set2)) != "" else print("None")]