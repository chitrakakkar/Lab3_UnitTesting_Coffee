import unittest
from Drinks import drink


class PriceTest(unittest.TestCase):
    def test_calculate_quantity_price(self):
        drink1 = drink("Coffee", "Large")
        expected = 5.45
        actual = drink1.calculate_price(1)
        self.assertEqual(expected, actual, "Large coffee should be 5.45 ")



