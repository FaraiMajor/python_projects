from art import logo

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
    "water": 700,
    "milk": 400,
    "coffee": 200,
}


def resource_sufficient(customer_order):
    for item in customer_order:
        if customer_order[item] > resources[item]:
            print(f"Sorry there is not enough {customer_order[item]}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(coins, drink_cost):
    if coins >= drink_cost:
        change = round(coins - drink_cost, 2)
        print(f'Here is your ${change} in change.')
        global sales
        sales += drink_cost
        return True
    else:
        print('Sorry thats not enough money. Money Refunded')
        return False


def dispense_coffee(drink_name, customer_order):
    for item in customer_order:
        resources[item] -= customer_order[item]
    print(f'Here is your {drink_name}. ☕Enjoy!')


print(logo)
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == 'off':
        is_on == False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Sales: ${sales}")
    else:
        drink = MENU[choice]
        if resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction(payment, drink['cost']):
                dispense_coffee(
                    choice, drink['ingredients'])
