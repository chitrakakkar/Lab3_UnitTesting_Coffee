from unittest import TestCase
from food import *


class TestFood(TestCase):
    def test_isInteger(self):
        # tests if the entered number is an integer
        self.assertEqual(4, Food.get_int_quantity(4))
        self.assertFalse(4, Food.get_int_quantity(10))

    def test_isPositive(self):
        # tests if the entered number is a positive integer
        self.assertEqual(5, Food.get_positive_quantity(5))
        self.assertFalse(-5, Food.get_positive_quantity(-5))

    def test_dictionary(self):
        food1 = Food("chips")
        dict1 = {"pizza-slice": 4.55,
                 "muffins": 3.78,
                 "crackers": 4.23,
                 "chips": 2.00,
                 "cookies":  3.63,
                 "ice-cream": 3.15}
        # self.assertEqual(dict1, Food.get_products())
        self.assertDictEqual(dict1, Food.get_products(food1))

    def test_food_list(self):
        expected = sorted(["pizza-slice",
                           "muffins",
                           "crackers",
                           "chips",
                           "cookies",
                           "ice-cream"])
        actual = sorted(list(Food.products.keys()))
        self.assertListEqual(expected, actual, " The list should be equal")
