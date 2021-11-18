num = int(input("Welcome to the game.\nHow many players are going to play? "))
def phrase_loop(num):
    while(True):
        for i in range(1, num+1):
            yield i
gen = phrase_loop(num)
print("Ok, the game starts.")
while True:
    x = input()
    if x == "":
        print("Player", next(gen), "turn.", end = "")