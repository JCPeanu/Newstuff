x = input("Enter a word: ")
Contains = False
for i in range (len(x)):
    if x[i] == 'o':
        for j in range(i, len(x)):
            if (x[j] == 'n'):
                for l in range(j, len(x)):
                    if (x[l] == 'e'):
                        print("The word contains 'one'.")
                        exit
    if x[i] == 't':
        for j in range(i, len(x)):
            if (x[j] == 'w'):
                for l in range(j, len(x)):
                    if (x[l] == 'o'):
                        print("The word contains 'two'.")
                        exit()
            elif (x[j] == "h"):
                for l in range(j, len(x)):
                    if (x[l] == 'r'):
                        for k in range(l, len(x)):
                            if (x[k] == 'e'):
                                for m in range(k, len(x)):
                                    if (x[m] == 'e'):
                                        print("The word contains 'three'.")
                                        exit()
            elif (x[j] == 'e'):
                for l in range(j, len(x)):
                    if (x[l] == 'n'):
                        print("The word contains 'ten'.")
                        exit()
    if x[i] == 'f':
        for j in range(i, len(x)):
            if (x[j] == 'o'):
                for l in range(j, len(x)):
                    if (x[l] == 'u'):
                        for k in range(l, len(x)):
                            if (x[k] == 'r'):
                                print("The word contains 'four'.")
                                exit()
            elif (x[j] == 'i'):
                for l in range(j, len(x)):
                    if (x[l] == 'v'):
                        for k in range(l, len(x)):
                            if (x[k] == 'e'):
                                print("The word contains 'five'.")
                                exit()
    if (x[i] == 's'):
        for j in range(i, len(x)):
            if (x[j] == 'i'):
                for l in range(j, len(x)):
                    if (x[l] == 'x'):
                        print("The word contains 'six'.")
                        exit()
            elif (x[j] == "e"):
                for l in range(j, len(x)):
                    if (x[l] == 'v'):
                        for k in range(l, len(x)):
                            if (x[k] == 'e'):
                                for m in range(k, len(x)):
                                    if (x[m] == 'n'):
                                        print("The word contains 'seven'.")
                                        exit()
    if (x[i] == 'e'):
        for j in range(i, len(x)):
            if (x[j] == 'i'):
                for l in range(j, len(x)):
                    if (x[l] == 'g'):
                        for k in range(l, len(x)):
                            if (x[k] == 'h'):
                                for m in range(k, len(x)):
                                    if (x[m] == 't'):
                                        print("The word contains 'eight'.")
                                        exit()
    if (x[i] == 'n'):
        for j in range(i, len(x)):
            if (x[j] == 'i'):
                for l in range(j, len(x)):
                    if (x[l] == 'n'):
                        for k in range(l, len(x)):
                            if (x[k] == 'e'):
                                print("The word contains 'nine'.")
                                exit()
print("The word is not a digit word.")

                        
