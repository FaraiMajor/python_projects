resources = {
    'water': 500,
    'milk': 500,
    'coffee_beans': 50,
    'cups': 5
}

drinks = {
    'espresso': {
        'ingredients': {
            'water': 250,
            'coffee_beans': 16
        },
        'price': 1.50
    },
    'latte': {
        'ingredients': {
            'water': 350,
            'milk': 75,
            'coffee_beans': 20
        },
        'price': 3.00
    },
    'cappuccino': {
        'ingredients': {
            'water': 200,
            'milk': 100,
            'coffee_beans': 12
        },
        'price': 2.50
    }
}


class CoffeeMachine:
    def __init__(self, resources, drinks):
        self.resources = resources
        self.drinks = drinks
        self.balance = 0

    def check_resources(self, drink_name):
        drink = self.drinks[drink_name]
        for ingredient, quantity in drink['ingredients'].items():
            if self.resources[ingredient] < quantity:
                return False
        return True

    def make_drink(self, drink_name):
        if not self.check_resources(drink_name):
            print("Sorry, we don't have enough resources to make that drink.")
            return

        drink = self.drinks[drink_name]
        for ingredient, quantity in drink['ingredients'].items():
            self.resources[ingredient] -= quantity

        self.balance += drink['price']
        print("Enjoy your {}! Your balance is now {}.".format(
            drink_name, self.balance))

    def take_money(self, amount):
        self.balance += amount


coffee_machine = CoffeeMachine(resources, drinks)
coffee_machine.take_money(10.00)
coffee_machine.make_drink('espresso')
coffee_machine.make_drink('latte')
coffee_machine.make_drink('cappuccino')
