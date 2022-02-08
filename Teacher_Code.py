import csv
import random
 
words_in_english = open("Josh.txt", "r")
all_words = list()
previous_word = " "
last_word_reached = False
while not last_word_reached:
    current_word = words_in_english.readline()
    current_word = current_word.rstrip("\n")
    if current_word == previous_word:
        last_word_reached = True
    else:
        all_words.append(current_word)
    previous_word = current_word
words_in_english.close()
 
print("This code will create csv files that have 10 rows and 10 columns each, filled with random words.")
number_of_files = int(input("How many files would you like to generate? "))
 
for file_number in range(number_of_files):
    file_name = f"file_{file_number}.csv"
    current_csv_file = open(file_name, 'w', newline='')
    for row in range(10):
        current_row = list()
        for word in range(10):
            current_row.append(random.choice(all_words))
        csv.writer(current_csv_file).writerow(current_row)
    current_csv_file.close()
 
print("\nDone.")