""" Unit testing file for validation method """

from unittest import TestCase
from validator import *


class TestValidator(TestCase):

    def test_get_user_int(self):
        # test if any string has been input
        self.assertTrue(get_string_input("Hello"))
        # test if any empty string has been input
        self.assertFalse(get_string_input(""))



