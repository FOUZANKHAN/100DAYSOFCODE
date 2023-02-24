#TODO:2 DO THIS KEEP track of resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money":0,
}

def butcher_name(name):
    ft = ""
    for i in range(len(name)):
        if name[i] == 'a' or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":
            ft +='o'
        ft+=name[i]
    return ft

def get_resources(drink):
    water = MENU[drink]["ingredients"]["water"]
    milk = MENU[drink]["ingredients"]["milk"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    return water, milk, coffee


def remove_resources(water, milk, coffee):
    if water < resources["water"] and milk < resources["milk"] and coffee < resources["coffee"]:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        return True
    else:
        print("Not enough resources")
        return False


def report_status():
    print("Okayrina sai gosoginsama")
    print(f'Water in machine = {resources["water"]}')
    print(f'Milk in machine = {resources["milk"]}')
    print(f'Coffee in machine = {resources["coffee"]}')
    print(f'Money in machin = {resources["money"]}')


def get_price_money(drink, quarters, dimes, nickels, pennies):
    money_given = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    money = MENU[drink]["cost"]
    if money > money_given:
        return -1
    else:
        final = money_given - money
        return final


def play_coffee():
    flag = True
    while flag:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        user_name = input("Give me your name: ").lower()
        fuser = butcher_name(user_name)
        if user_input.startswith("o") or user_name.startswith("o"):
            exit()
        elif user_input.startswith("r"):
            report_status()
        else:
            w, m, c = get_resources(user_input)
            resources_status = remove_resources(w, m, c)
            if not resources_status:
                flag = False
                break
            print("Please insert coins")
            q = int(input("How many quarters:? "))
            d = int(input("How many dimes:?  "))
            n = int(input("How many nickels:?  "))
            p = int(input("How many pennies:?  "))
            f = get_price_money(user_input, q, d, n, p)
            if f == -1:
                flag = False
            resources["money"] += MENU[user_input]["cost"]
            print(f"Here is ${round(f,3)} in change")
            print(f"Here is your {user_input} {fuser} Enjoy Fam!")


play_coffee()


