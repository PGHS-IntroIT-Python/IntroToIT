# -*- coding: utf-8 -*-
__author__ = 'kajigga'

import unittest
from function_libs import *


class FunctionTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(68, celsiusToFahrenheit(20))
        self.assertEqual(50, celsiusToFahrenheit(10))
        self.assertEqual(-40, celsiusToFahrenheit(-40))

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(-7, fahrenheitToCelsius(20))
        self.assertEqual(-13, fahrenheitToCelsius(10))
        self.assertEqual(-40, fahrenheitToCelsius(-40))

    def test_calculate_circumference_of_circle(self):
        self.assertEqual(12.56, circumferenceOfCircle(2))
        self.assertEqual(75.36, circumferenceOfCircle(12))
        self.assertEqual(34.54, circumferenceOfCircle(5.5))
        self.assertEqual(43.96, circumferenceOfCircle(7))

    def test_calculate_area_of_a_circle(self):
        self.assertEqual(12.56, areaOfCircle(2))
        self.assertEqual(314, areaOfCircle(10))
        self.assertEqual(94.985, areaOfCircle(5.5))
        self.assertEqual(153.86, areaOfCircle(7))

import random,string
class StringTests(unittest.TestCase):
    def randomString(self):
        return ''.join(random.choice(string.ascii_uppercase) for i in range(12))
    def test_returns_theSameStringDoubled(self):
        r_string = self.randomString()
        self.assertEqual(r_string*2,returnSameStringDoubled(r_string))

    def test_returns_someStringThatIs_N_charactersLong(self):
        self.assertEqual(20,len(someStringThatIsNCharactersLong(20)))

class NumberTests(unittest.TestCase):
    def random_number(self):
        return random.choice(range(1, 10000))
    def test_returns_a_number(self):
        self.assertIsInstance(returnsANumber(),int)

    def test_returns_number_squared(self):
        number = 25
        number_squared = number ** 2
        self.assertEqual(number_squared,getNumberSquared(number))

    def test_returns_remainder_of_two_numbers_divided(self):
        number1 = self.random_number()
        number2 = self.random_number()
        remainder = number1 % number2
        self.assertEqual(remainder,getRemainder(number1,number2))

