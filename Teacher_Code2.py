import csv
 
search_for_this_word = input("Which word are you looking for? ")
word_found = False
 
try:
    for file_number in range(100):
        file_name = f"file_{file_number}.csv"
        current_csv_file = open(file_name, 'r', newline='')
        count = 1
        for row in csv.reader(current_csv_file):
            for word in row:
                if word == search_for_this_word:
                    print(f"The word {search_for_this_word} is in file {current_csv_file}, in row {count}.")
                    word_found = True
            count += 1
        current_csv_file.close()
except:
    print("\nAll files searched.")
else:
    print("\nNumber of files is not enough, please increase the iterator quantity in the code.")
finally:
    if not word_found:
        print("\nThe word does not appear to exist in the files...")
    print("Ending program.")