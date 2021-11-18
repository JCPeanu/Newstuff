fn = input("What's your first name? ")
ln = input("What's your last name? ")
fn1 = int(len(fn)/2)
ln1 = int(len(ln)/2)
print("Hmm... I'm going to assign you two nicknames ;-)")
fn = fn[0].upper()+fn[1:]
ln = ln[0].upper()+ln[1:]
x = fn[0:fn1]+ln[ln1:]
y = ln[0:ln1] + fn[fn1:]
print(f"The first one is '{x}'.")
print(f"The second one is '{y}'.")
print("Hope you like them!")
