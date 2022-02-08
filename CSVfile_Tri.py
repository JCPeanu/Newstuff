import csv
print("This code will create csv files that have an inverted isosceles pyramid, and the user provides the height.")
height = int(input("Pyramid's height: "))

file_name = f"InvertedTriangle.csv"
current_csv_file = open(file_name, 'w', newline='')
for row in range(1, height + 1):
    lst = []
    for j in range(row):
        lst.append(",")
    lst.append("\\")
    for j in range(2*(height - row)):
        lst.append("-")
    lst.append("/")
    for j in range (row):
        lst.append(",")
    csv.writer(current_csv_file).writerow(lst)
print("\nDone.")