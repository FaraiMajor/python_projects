class CoffeeMaker:

    def __init__(self):
        self.resources = {
            'water': 700,
            'milk': 500,
            'coffee': 300,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def resource_sufficient(self, drink):
        """Check if there are sufficient ingredients to make the drink"""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_drink(self, order):
        """Deducts used resources from available resources"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy")
