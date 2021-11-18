print("Welcome to Josh's Restaurant")
x = input("What is your name? ")
print(f"Welcome {x}")
eggs = int(input("How many fried eggs do you want to eat? "))
numeggs = 30
burger = int(input("How many double cheese burger do you want to eat? "))
numburger = 300
veg = int(input("How many servings do you want for blanching vegetables? "))
numveg = 100
print("...")
print("Thank you for eating at Josh's Restaurant.\n")
print("Your take from the menu today was: ")
print("{:<30}{:<15}{:<10}".format("Dish","Quantity","Price per Unit")) 
print("Fried eggs".ljust(30,"."), str(eggs).ljust(15, "."), str(numeggs).ljust(15, "."), sep = '')
print("Doubole Cheese Burger".ljust(30,"."), str(burger).ljust(15, "."), str(numburger).ljust(15, "."), sep = '')
print("Blanching vegetables".ljust(30,"."), str(veg).ljust(15, "."), str(numveg).ljust(15, "."), sep = '')
total = int((eggs*numeggs)+(burger*numburger)+(veg*numveg))
tax = float(total * 0.07)
tip = float(total*0.18)
subtotal = float(total + tax + tip)
print("{}{:<18}{}{:<8}{}{}".format("Subtotal: $", format(total, '.2f'), " Tax: $", format(tax, '.2f'), " Tip: ", format(tip, '.2f')))
print(f"Total: ${format(float(subtotal), '.2f')}")

