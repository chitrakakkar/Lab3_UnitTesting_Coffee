class Drink:
    products = {"coffee": [5.45, 4.15, 3.25],
                "mocha": [10, 3.78, 2.65],
                "tea": [4.23, 3.34, 2.54],
                "cappuccino": [4.85, 3.28, 2.95],
                "espresso": [4.35, 3.63, 2.45]}

    sizes = ("LARGE", "MEDIUM", "SMALL")

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @staticmethod
    def get_products():
        return Drink.products

    @staticmethod
    def get_sizes():
        return Drink.sizes

    def calculate_price(self, quantity):
        """ The prices are listed like 'Large','Medium','Small'
         'Look -up is the index of price ar per the size """

        if str(self.size).strip(" ").upper() == 'LARGE':
            lookup = 0
        elif self.get_size__upper_case(self.size) == 'MEDIUM':
            lookup = 1
        else:
            lookup = 2
        for key, data in self.products.items():
            if key == str(self.name).strip(" ").lower():
                total_price = self.get_int_quantity(quantity) * self.products[key][lookup]
                return total_price

    @staticmethod
    def get_int_quantity(quantity):
        return int(quantity)

    @staticmethod
    def get_size__upper_case(size):
        return str(size).strip(" ").upper()

    @staticmethod
    def get_positive_quantity(quantity):
        return abs(quantity)






