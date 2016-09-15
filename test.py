import unittest
from Drinks import Drink


class PriceTest(unittest.TestCase):
    def test_calculate_quantity_price(self):
        drink1 = Drink("Coffee", "Large")
        expected = 5.45
        actual = drink1.calculate_price(1)
        self.assertEqual(expected, actual, "Large coffee should be 5.45 ")


    def test_size_upper_Case(self):
        drink1 = Drink("Mocha", "Medium")
        expected = str(drink1.size).upper()
        actual = drink1.get_size__upper_case(drink1.size)
        self.assertEqual(expected, actual, " Size should be upper case ")

