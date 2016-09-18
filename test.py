""" This tests the possible bugs in the program"""

import unittest
from drink import Drink


class PriceTest(unittest.TestCase):
    def test_calculate_quantity_price(self):
        drink1 = Drink("Coffee", "Large")
        expected = 5.45
        actual = drink1.calculate_price(1)
        self.assertEqual(expected, actual, "Large coffee should be 5.45 ")

    def test_size_upper_Case(self):
        drink1 = Drink("Mocha", "Medium")
        expected = "MEDIUM"
        actual = drink1.get_size__upper_case(drink1.size)
        self.assertEqual(expected, actual, " Size should be upper case ")

    def test_quantity_int(self):
        drink1 = Drink("Tea", "Small")
        expected = 2
        actual = drink1.get_int_quantity(2)
        self.assertEqual(expected, actual, " Quantity should be an integer")

    def test_positive_quantity(self):
        drink1 = Drink(" Cappuccino", " Large")
        expected = 1
        actual = drink1.get_positive_quantity(1)
        self.assertEqual(expected, actual, " Quantity should be positive integer")
