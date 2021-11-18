print("I will use the letters you inputed and create a fibonacci sequence corresponding to the sequence of the letter in the alphabet.")
ch1 = ord(input("Please enter a capitalized letter: "))
ch2 = ord(input("Please enter another capitalized letter: "))
c = 0
i = 0
while (i < 10):
    print (chr(ch1), " ", end = "", sep=",")
    c = ch1
    ch1 = ch2
    ch2 = ((ch1%64 + c%64)%26)+64
    i += 1
print("\b\b.")
print("Thank you for using this code.")
