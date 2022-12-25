from art import logo
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

print(logo)

is_on = True
while is_on:

    choice = input(f'What would you like? ({menu.get_items()}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        # retrive drink from menu module
        drink = menu.find_drink(choice)
        # check if we have sufficient ingredients for the drink
        if coffe_maker.resource_sufficient(drink):
            print(f"Please insert ${drink.cost}.")
            # check if we have enough money for the drink then make the drink
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_drink(drink)
