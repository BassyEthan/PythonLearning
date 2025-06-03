import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 0.0,
}

def process_coins():
    quarters = int(input("How many quarters would you like to add: "))
    dimes = int(input("How many dimes would you like to add: "))
    nickles = int(input("How many nickles would you like to add: "))
    pennies = int(input("How many pennies would you like to add: "))
    total = (quarters * 25 + dimes * 10 + nickles * 5 + pennies)/100
    resources["money"] = total

def check_resources(drink):
    if resources["water"] >= MENU[drink]["ingredients"]["water"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        if resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
            if resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
                resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                print(f"Water: {resources['water']} ml")
                print(f"Milk: {resources['milk']} ml")
                print(f"Coffee: {resources['coffee']} g")
                print("-------------------------------------")
                process_coins()

                if resources["money"] < MENU[drink]["cost"]:
                    print("Sorry, that's not enough money. Money refunded")
                elif resources["money"] >= MENU[drink]["cost"]:
                    resources["money"] = resources['money'] - MENU[drink]["cost"]
                    print(f"Here is ${resources['money']:.2f} in change.")
                    print(f"Here is your {drink}. Enjoy!")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough milk")
    else:
        print("Sorry there is not enough water")


keep_playing = True
while keep_playing:
    prompt = input("What would you like? (espresso, latte, cappuccino): ")
    if prompt == "off":
        keep_playing = False
        sys.exit()
    elif prompt == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]} ")
    elif prompt in ["espresso", "latte", "cappuccino"]:
        check_resources(prompt)
    else:
        print("Try again - you did not enter one of the options.")