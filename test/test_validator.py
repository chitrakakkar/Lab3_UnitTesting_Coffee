""" Unit testing file for validation method """

from unittest import TestCase
from validator import *


class TestValidator(TestCase):
    def test_get_user_string(self):
        # test if any string input are equal
        self.assertEqual("Hello", get_string1_input("Hello"))
        # test if any string input are equal
        self.assertEqual("Capstone", get_string1_input("Capstone"))
        # test if the string input are not equal
        self.assertNotEqual("  ", get_string1_input(""))
        # test if the string input are not equal
        self.assertNotEqual(" Java ", get_string1_input("C#"))

    def test_get_int(self):
        # test if an integer is returned
        self.assertEqual(2, is_int(2)[1])
        # test if an integer is returned
        self.assertEqual(1001, is_int(1001)[1])
        # test if an integer is not equal
        self.assertNotEqual(3, is_int(1)[1])
        # test if an integer is not equal
        self.assertNotEqual(999, is_int(99)[1])
        # should be false as we need integer greater than 0
        self.assertFalse(is_int(0)[1])
        self.assertTrue(is_int(5)[0])
        self.assertTrue(is_int(100)[0])


    def test_is_whole_number(self):
        # check that whole numbers with correct range passes
        self.assertTrue(is_whole_number(2, range(0, 3)))
        self.assertTrue(is_whole_number(-9, range(-10, 10)))
        self.assertTrue(is_whole_number(999,range(0, 1000)))
        self.assertTrue(is_whole_number(12, range(0, 13)))
        self.assertTrue(is_whole_number(-3, range(-5, 5)))
        # check that invalid ranges return false
        self.assertFalse(is_whole_number(-2, range(0, 3)))
        self.assertFalse(is_whole_number(7, range(-5, 5)))
        # check that floats return false, including with both valid and invalid ranges
        self.assertFalse(is_whole_number(4.345, range(0, 3)))
        self.assertFalse(is_whole_number(-.412, range(5, 6)))
        self.assertFalse(is_whole_number(-.05, range(1, 5)))
        self.assertFalse(is_whole_number(12.0, range(-1, 5)))




