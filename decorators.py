def hangman():
    return "Let's play hangman!"

def tic_tac_toe():
    return "Let's play tic-tac-toe!"

def play_Game(func):
    for i in range(40):
        print("*", end = "")
    print()
    for j in range(40):
        print("%", end = "")
    x = "Let's play " + func + "!"
    print("\n", x.center(40))
    for i in range(40):
        print("%", end = "")
    print()
    for j in range(40):
        print("*", end = "")
print("Please enter either hangman or tic_tac_toe and I will display we will play that game.")
gm = input("Do you want to play hangman or tic_tac_toe?")
play_Game(gm)
