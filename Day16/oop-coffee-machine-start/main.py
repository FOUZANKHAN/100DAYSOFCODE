from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_instance = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have?({options}):  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        machine_instance.report()
    else:
        drink = menu.find_drink(choice)
        if machine_instance.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            #print("Latte? Kaiku nai laate")
            machine_instance.make_coffee(drink)



