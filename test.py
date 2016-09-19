""" This tests the possible bugs in the program"""

import unittest
from drink import Drink
from main import *


class PriceTest(unittest.TestCase):
    # tests the quantity of the large coffee is 5.45
    # can test that for each drink for each size
    def test_calculate_quantity_price(self):
        drink1 = Drink("Coffee", "Large")
        expected = 5.45
        actual = drink1.calculate_price(1)
        self.assertEqual(expected, actual, "Large coffee should be 5.45 ")

    def test_size_upper_Case(self):
        # tests if the size entered is in upper-case
        drink1 = Drink("Mocha", "Medium")
        expected = "MEDIUM"
        actual = drink1.get_size__upper_case(drink1.size)
        self.assertEqual(expected, actual, " Size should be upper case ")

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
        drink1 = Drink("Mocha", " Small")
        expected = 2.65
        actual = drink1.products["mocha"][2]
        self.assertEqual(expected,actual, " The price for small mocha should be $2.65")

    def valid_drink_check(self):
        drink1 = Drink("Tea", "Medium")
        expected = ["coffee", "mocha", "tea", "cappuccino", "espresso"]
        actual = (drink1.products.keys())
        self.assertListEqual(expected, actual)




