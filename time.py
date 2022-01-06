import time
import random

def game():
    num = random.randint(2, 7)
    print("The time is", num,"seconds")
    print("The game is going to start off in ")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1")
    start = time.time()
    x = input()
    final = time.time()
    diff = final - start
    if (abs(diff - num) <= 0.2):
        print("Diff: ", round(diff, 2))
        print("You are the master of time!")
    elif (abs(diff - num) <= 0.5):
        print("Diff: ", round(diff, 2))
        print("Very good sense of time!")
    elif (abs(diff - num) <= 0.7):
        print("Diff: ", round(diff, 2))
        print("Not bad timing.")
    else:
        print("Diff: ", round(diff, 2))
        print("That was awful.")
game()
