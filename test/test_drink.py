from unittest import TestCase
from main import *


class TestDrink(TestCase):
    def test_calculate_quantity_price(self):
        drink1 = Drink("Coffee", "Large")
        expected = 5.45
        actual = drink1.calculate_price(1)
        self.assertEqual(expected, actual, "Large coffee should be 5.45 ")

    def test2_calculate_quantity_price(self):
        drink1 = Drink("Tea", "small")
        expected = 5.08
        actual = drink1.calculate_price(2)
        self.assertEqual(expected, actual, "Large coffee should be 5.45 ")

    def test_quantity_int(self):
        # checks if the quantity is an integer
        drink1 = Drink("Tea", "Small")
        expected = 2
        actual = drink1.get_int_quantity(2)
        self.assertEqual(expected, actual, " Quantity should be an integer")

    def test_positive_quantity(self):
        # Quantity should be +ve
        drink1 = Drink(" Cappuccino", " Large")
        expected = 1
        actual = drink1.get_positive_quantity(1)
        self.assertEqual(expected, actual, " Quantity should be positive integer")

    def test_valid_price_check(self):
        # checks if the object has valid price
        drink1 = Drink("Mocha", " Small")
        expected = 2.65
        actual = drink1.products["mocha"][2]
        self.assertEqual(expected, actual, " The price for small mocha should be $2.65")

    def test_size_upper_Case(self):
        # tests if the size entered is in upper-case
        drink1 = Drink("Mocha", "Medium")
        expected = "MEDIUM"
        actual = drink1.get_size__upper_case(drink1.size)
        self.assertEqual(expected, actual, " Size should be upper case ")

    def test_valid_drink_check(self):
        # tests if the drink name is valid
        drink1 = Drink("Tea", "Medium")
        expected = sorted(["coffee", "mocha", "tea", "cappuccino", "espresso"])
        actual = sorted(list(drink1.products.keys()))
        self.assertListEqual(expected, actual, " The list should be equal")

    # tests that the products each have 3 prices
    def test_products_have_three_prices(self):
        # should return a dictionary of drinks.
        drink_dict = Drink.get_products()
        for drink in drink_dict:
            self.assertEqual(len(drink_dict[drink]), 3, 'There should be three prices in each drink.')

    # tests that the products each valid prices greater 0 > 10
    def test_products_prices_of_drinks_greater_than_zero(self):
        # should return a dictionary of drinks.
        drink_dict = Drink.get_products()
        for drink in drink_dict:
            for price in drink_dict[drink]:
                self.assertTrue(price > 0, 'Each price should be greater than 0.')

    def test_products_prices_of_drinks_lass_than_ten_dollars(self):
        # should return a dictionary of drinks.
        drink_dict = Drink.get_products()
        for drink in drink_dict:
            for price in drink_dict[drink]:
                self.assertTrue(price < 10, 'Each price should be less than 10.')

    def test_valid_product_list(self):
        drink1 = Drink("Mocha", "Small")
        dict1 = {"coffee": [5.45, 4.15, 3.25],
                 "mocha": [4.65, 3.78, 2.65],
                 "tea": [4.23, 3.34, 2.54],
                 "cappuccino": [4.85, 3.28, 2.95],
                 "espresso": [4.35, 3.63, 2.45]}
        actual = Drink.get_products(drink1)
        self.assertEqual(dict1, actual, "Product list has some error")

if __name__ == '__main__':
    TestCase.main()
