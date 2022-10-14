from unittest import TestCase
from main import *


class Test(TestCase):
    def test_celcius_to_fahrenheit(self):
        self.assertEqual(celcius_to_fehrenheit(20), 68.0)
