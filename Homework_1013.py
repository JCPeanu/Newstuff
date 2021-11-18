reference = {'pa' : '1', "re": '2', "ci" : '3', "vo" : '4', "mu": '5', "xa": '6', "ze" : '7', "bi" : '8', "so" : '9', "no" : '0'}
inp = input("Please enter two lojban sequence with the + sign in between and I will give you the sum of them: ")
set1 = set(i.strip() for i in inp.split("+"))
total = 0
ans = ""
for x in set1:
    num = ""
    for i in range(0, len(x), 2):
        num += reference.get(x[i: i+2])
    total += int(num)
keys = list(reference.keys())
values = list(reference.values())
for j in range(0, len(str(total))):
    z = str(total)[j]
    ans += keys[values.index(str(z))]
print(ans)