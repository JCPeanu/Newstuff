import csv

# outputFile = open('example.csv', 'w', newline = '')
# csv.writer(outputFile).writerow(['ABC', '123', 123])
# csv.writer(outputFile).writerow(['DEF', '456', 456])
# outputFile.close()

inputFile = open('example.csv', 'r', newline = '')
for row in csv.reader(inputFile):
    print(row)
inputFile.close()