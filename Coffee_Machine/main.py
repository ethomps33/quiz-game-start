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

# for resource in resources:
#     print(f"{resource}: {resources[resource]}ml")

# TODO: 2 Print the prices of all the coffee available

print("MENU")
for item in MENU:
    print(f"{item} price: ${MENU[item]['cost']}")


# TODO: 4 Create If Statements to check if there are available resources for the order
# Create function to "brew" the coffee

def brew(order):
    if order == 'espresso':
        avail = True
        for ingr, quant in MENU[order]["ingredients"].items():
            if resources[ingr] < quant:
                print(f"There is not enough {ingr} available.")
                avail = False
        if avail:
            for ingr, quant in MENU[order]["ingredients"].items():
                resources[ingr] -= quant
                return order

    if order == 'latte':
        avail = True
        for ingr, quant in MENU[order]["ingredients"].items():
            if resources[ingr] < quant:
                print(f"There is not enough {ingr} available.")
                avail = False
        if avail:
            for ingr, quant in MENU[order]["ingredients"].items():
                resources[ingr] -= quant
                return order

    if order == 'cappuccino':
        avail = True
        for ingr, quant in MENU[order]["ingredients"].items():
            if resources[ingr] < quant:
                print(f"There is not enough {ingr} available.")
                avail = False
        if avail:
            for ingr, quant in MENU[order]["ingredients"].items():
                resources[ingr] -= quant
                return order


# TODO: 5 Create a function that randomly generates coins in a 'wallet'

import random

wallet = {'quarter': 0,
          'dime': 0,
          'nickel': 0,
          'penny': 0,
          }


def caching():
    for coin in wallet:
        wallet[coin] = random.randint(0, 20)
    print(f"This is the money in your wallet:\n {wallet}")


# TODO: 6 Create a function that calculates the coins inserted to pay for item and returns change

def paying(selection):
    price = MENU[selection]['cost']
    payment = {'quarter': 0,
               'dime': 0,
               'nickel': 0,
               'penny': 0,
               }

    broke = False

    for coin in payment:
        payment[coin] = int(input(f"How many {coin}s?: "))
        if payment[coin] > wallet[coin]:
            print(f"You don't have that many {coin}s")
            broke = True
            break


    total = 0
    if broke == False:
        for coin in payment:
            if coin == 'quarter':
                total += (payment[coin] * .25)
                wallet[coin] -= payment[coin]
            elif coin == 'dime':
                total += (payment[coin] * .10)
                wallet[coin] -= payment[coin]
            elif coin == 'nickel':
                total += (payment[coin] * .05)
                wallet[coin] -= payment[coin]
            elif coin == 'penny':
                total += (payment[coin] * .01)
                wallet[coin] -= payment[coin]

    if total >= price:
        total -= price
        print(f"Here is ${round(total, 2)} in change.")
        if total % .25:
            wallet['quarter'] += total/.25
        elif total % .10:
            wallet['dime'] += total/.10
        elif total % .05:
            wallet['nickel'] += total/.05
        elif total % .01:
            wallet['penny'] += total/.01
        print(f"Enjoy your {order} ☕!")
    elif total < price:
        print("Sorry, that's not enough money for this drink.")

    addtl = input("Do you want something else? 'y' or 'n': ")
    if addtl == 'y':
        print(f"This is the money in your wallet:\n {wallet}")
        order2 = input("What is your order? 'Espresso'/'Latte'/'Cappuccino': ").lower()
        selection = brew(order2)
        paying(selection)

caching()
# TODO: 3 Ask user what drink they want to order
# Create an input statement to retrieve user order

global order
order = input("What is your order? 'Espresso'/'Latte'/'Cappuccino': ").lower()

selection = brew(order)
paying(selection)
