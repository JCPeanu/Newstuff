def infinite_loop(wrd):
    wrd = wrd.split()
    print(wrd)
    while(True):
        for i in wrd:
            yield i

func = infinite_loop("dkdjd slei")

while True:
    x = input()
    if x == '':
        print(next(func))