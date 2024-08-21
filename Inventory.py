from datetime import datetime
from Ingredient import Ingredient

class Inventory:
    def __init__(self):
        self.ingredients = {}
        self.usage_log = []

    # Add ingredient
    def add_ingredient(self, name, quantity, unit, low_stock_threshold=5):
        name = name.lower()  # Convert to lowercase
        if name in self.ingredients:
            self.ingredients[name].quantity += quantity
        else:
            self.ingredients[name] = Ingredient(name, quantity, unit, low_stock_threshold)

    # Remove ingredient 
    def remove_ingredient(self, name, quantity):
        name = name.lower()  # Convert to lowercase
        if name in self.ingredients:
            if self.ingredients[name].quantity >= quantity:
                self.ingredients[name].quantity -= quantity
                self.log_usage(name, quantity)
                print(f"{quantity} {self.ingredients[name].unit} of {name} have been removed succesfully\n")
                if self.ingredients[name].quantity == 0:
                    del self.ingredients[name]
            else:
                print(f"Not enough {name} in stock to remove {quantity}.\n")
        else:
            print(f"{name.capitalize()} not found in inventory.\n")

    # Update ingredient
    def update_ingredient(self, name, quantity, unit=None, low_stock_threshold=None):
        name = name.lower()  # Convert to lowercase
        if name in self.ingredients:
            self.ingredients[name].quantity = quantity
            if unit:
                self.ingredients[name].unit = unit
            if low_stock_threshold is not None:
                self.ingredients[name].low_stock_threshold = low_stock_threshold
        else:
            print(f"{name.capitalize()} not found in inventory.")

    # Check ingredient
    def get_ingredient(self, name):
        name = name.lower()  # Convert to lowercase
        return self.ingredients.get(name, f"{name.capitalize()} not found in inventory.")

    # List inventory
    def list_ingredients(self):
        return [str(ingredient) for ingredient in self.ingredients.values()]

    # Feature 1: Low Stock Alerts
    def check_low_stock(self):
        low_stock_items = [str(ingredient) for ingredient in self.ingredients.values() if ingredient.is_low_stock()]
        if low_stock_items:
            print("Low Stock Alert:")
            for item in low_stock_items:
                print(item)
        else:
            print("All stock levels are sufficient.")

    # Feature 2: Usage Log
    def log_usage(self, name, quantity):
        name = name.lower()  # Ensure name is logged in lowercase
        self.usage_log.append(f"{datetime.now()}: Used {quantity} of {name.capitalize()}")

    def view_usage_log(self):
        return self.usage_log

    # Feature 3: Reporting 
    def generate_report(self):
        print("\n--- Inventory Report ---")
        print("Current Stock Levels:")
        for ingredient in self.list_ingredients():
            print(ingredient)

        print()
        self.check_low_stock()

        print("\nUsage Log:")
        for log_entry in self.view_usage_log():
            print(log_entry)
        print("-----------------------\n")