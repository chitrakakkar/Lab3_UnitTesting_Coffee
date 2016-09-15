class drink():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def calculate_price(self, name, size, quantity):
        """ The prices are listed like 'Large','Medium','Small'
         'Look -up is the index of price ar per the size """

        products = {"coffee": [5.45, 4.15, 3.25],
                    "mocha": [4.65, 3.78, 2.65],
                    "tea": [4.23, 3.34, 2.54],
                    "cappuccino": [4.85, 3.28, 2.95],
                    "espresso": [4.35, 3.63, 2.45]}

        if str(size).strip(" ").upper() == 'LARGE':
            lookup = 0
        elif str(size).strip(" ").upper() == 'MEDIUM':
            lookup = 1
        else:
            lookup = 2
        for key, data in products.items():
            if key == str(name).strip(" ").lower():
                total_price = int(quantity) * products[key][lookup]
                return total_price








