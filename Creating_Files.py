file1 = open("newfile.txt", "w")
file1.write("3\n9")
file1.close()
file1 = open("newfile.txt", "r")
print("I will read the first number and the second number in the file and print out the sum and their product.")
line1 = int(file1.readline().strip("\n"))
line2 = int(file1.readline().strip("\n"))
print("Sum: ", end = "")
print(line1 + line2)
print("Product: ", end = "")
print(line1 * line2)
file1.close()