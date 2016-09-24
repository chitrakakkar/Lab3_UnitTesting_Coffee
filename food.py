""" this class contains a dictionary of snacks with price
calculate the price method
"""


class Food:
    products = {"pizza-slice": 4.55,
                "muffins": 3.78,
                "crackers": 4.23,
                "chips": 2.00,
                "cookies":  3.63,
                "ice-cream": 3.15}

    def __init__(self, name):
        self.name = name

    def get_products(self):
        return self.products

    def calculate_food_price(self, quantity):
        """ calculate the price for the snacks based on the quantity"""
        for key, data in self.products.items():
            if key == str(self.name).strip(" ").lower():
                total_price = self.get_int_quantity(quantity) * float(data)
                return total_price

    @staticmethod
    def get_int_quantity(quantity):
        return int(quantity)

    @staticmethod
    def get_positive_quantity(quantity):
        return abs(quantity)