''' cerintele sunt implementarea unui "aparat de cafea" care sa iti tina cont
de consumabile si bani pentru a da diferite tipuri de cafea cumparatorului,
pentru a putea retrage toti banii din aparat sau pentru a umple aparatul cu
consumabile'''
'''Am definit functiile pentru fiecare tip de actiune pe care sa il faca
aparatul de cafea, ca sa pot implementa astfel exercitiul:'''

def buy_drink (nec_water, nec_milk, nec_beans, nec_cups, nec_money):
    global water
    water -= nec_water
    global milk
    milk -= nec_milk
    global beans
    beans -= nec_beans
    global cups
    cups -= nec_cups
    global money
    money += nec_money
    return(water, milk, beans, cups, money)
'''acest tip de print functioneaza, adica imi returneaza valorile actualizate,
in functie de bautura selectata - mai jos cand invoc functia ii dau parametrii
necesari pentru fiecare tip de bautura'''

def take_money ():
    global money
    print(f" You have removed {money} dollars from the machine.")
    money -= money
'''acest tip de print functioneaza, adica imi returneaza valorile actualizate,
respectiv zero bani:'''

def fill_supplies ():
    water_fill = int(input("How much water do you want to fill with: "))
    global water
    water += water_fill
    milk_fill = int(input("How much milk do you want to fill with: "))
    global milk
    milk += milk_fill
    beans_fill = int(input("How much coffee do you want to fill with: "))
    global beans
    beans += beans_fill
    cups_fill = int(input("How many cups do you want to put in the machine: "))
    global cups
    cups += cups_fill
'''acest tip de print functioneaza, adica imi returneaza valorile actualizate,
in functie de ce anume dai sa umple la fiecare tip de consumabila'''

def print_satus():
    print(f"The machine now has: \n \
            {water} ml of water \n \
            {milk} ml of milk \n \
            {beans} grams of beans;\n \
            {cups} cups\n \
            {money} money")

'''aici sunt stocurile initiale date de problema:'''

water = 400
milk = 540
beans = 120
cups = 9
money = 550

'''aici, ca sa nu tot pun acel print formatat (ca mai sus in functie),
am facut un status al aparatului'''
status = f"The machine now has: \n \
        {water} ml of water \n \
        {milk} ml of milk \n \
        {beans} grams of beans;\n \
        {cups} cups\n \
        {money} money"

print(status)
command = (input("Do you want to buy some coffee, fill the machine or take out money? "))
print(command)
if command == "take":
    take_money()
elif command == "fill":
    fill_supplies()
elif command == "buy":
    coffee_type = input("Do you want an 1 - espresso, a 2 - latte or a 3 - cappuccino: ")
    if coffee_type == "1":
        buy_drink(250, 0, 16, 1, 4)
    elif coffee_type == "2":
        buy_drink(350, 75, 20, 1, 7)
    elif coffee_type == "3":
        buy_drink(200, 100, 12, 1, 6)

print_satus()
