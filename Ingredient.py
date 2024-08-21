class Ingredient:
    def __init__(self, name, quantity, unit, low_stock_threshold=5):
        self.name = name.lower()  # Convert to lowercase
        self.quantity = quantity
        self.unit = unit
        self.low_stock_threshold = low_stock_threshold

    def __repr__(self):
        return f"{self.name.capitalize()}: {self.quantity} {self.unit}"  # Capitalize for display

    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold