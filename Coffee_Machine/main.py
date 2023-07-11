# This is a sample Python script.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1 Print all of the coffee machine resources

for resource in resources:
    print(f"{resource}: {resources[resource]}ml")

#TODO: 2 Print the prices of all the coffee available

for item in MENU:
    print(f"{item} price: ${MENU[item]['cost']}")

#TODO: 3 Ask user what drink they want to order
#Create an input statement to retreive user order

order = input("What is your order? 'Espresso'/'Latte'/'Cappuccino': ").lower()

#TODO: 4 Create If Statements to check if there are available resources for the order

if order == 'espresso':
    avail = True
    for ingr,quant in MENU[order]["ingredients"].items():
        if resources[ingr] < quant:
            print("There are not enough resources available.")
            avail = False
    if avail:
        for ingr,quant in MENU[order]["ingredients"].items():
            resources[ingr] -= quant
            print(resources)

if order == 'latte':
    avail = True
    for ingr, quant in MENU[order]["ingredients"].items():
        if resources[ingr] < quant:
            print("There are not enough resources available.")
            avail = False
    if avail:
        for ingr, quant in MENU[order]["ingredients"].items():
            resources[ingr] -= quant
            print(resources)

if order == 'cappuccino':
    avail = True
    for ingr, quant in MENU[order]["ingredients"].items():
        if resources[ingr] < quant:
            print("There are not enough resources available.")
            avail = False
    if avail:
        for ingr, quant in MENU[order]["ingredients"].items():
            resources[ingr] -= quant
            print(resources)


