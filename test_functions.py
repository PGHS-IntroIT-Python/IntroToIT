# -*- coding: utf-8 -*-
__author__ = 'kajigga'
"""This file is full of tests. Tests that are run against your code. You will write
functions in function_libs.py to satisfy these tests. Do not worry about not
understanding what the code here is doing, just look for comments (lines that start
with "#". These lines will describe the functions you need to write.
"""

import unittest
from function_libs import *

class PGHS_TestingGame(unittest.TestCase):
    score = 0
    def __init__(self,*args,**kwargs):
       super(PGHS_TestingGame,self).__init__(*args,**kwargs)
    def randomString(self,length=12):

        return ''.join(random.choice(string.punctuation+string.digits+string.ascii_letters) for i in range(length))
    def random_number(self,minimum=1,maximum=101):
        return random.choice(range(minimum, maximum))
    
class FunctionTests(PGHS_TestingGame):
    def test_celsius_to_fahrenheit(self):
        # Write a function called celsiusToFahrenheit. This function should take one parameter, the celsius number
        # and return the fahrenheit temperature
        self.assertEqual(68, celsiusToFahrenheit(20))
        self.assertEqual(50, celsiusToFahrenheit(10))
        self.assertEqual(-40, celsiusToFahrenheit(-40))



    def test_fahrenheit_to_celsius(self):
        # Write a function called fahrenheitToCelsius. This function should take one parameter, the fahrenheit number
        # and return the celsius temperature
        self.assertEqual(-7, fahrenheitToCelsius(20))
        self.assertEqual(-13, fahrenheitToCelsius(10))
        self.assertEqual(-40, fahrenheitToCelsius(-40))
        self.score +=1

    def test_calculate_circumference_of_circle(self):
        # Write a function called circumferenceOfCircle. This function should take one
        # parameter, the radius, and return the circumference
        self.assertEqual(12.56, circumferenceOfCircle(2))
        self.assertEqual(75.36, circumferenceOfCircle(12))
        self.assertEqual(34.54, circumferenceOfCircle(5.5))
        self.assertEqual(43.96, circumferenceOfCircle(7))
        self.score +=1

    def test_calculate_area_of_a_circle(self):
        # Write a function called areaOfCircle. This function should take one parameter,
        # the radius, and return the area of the circle
        self.assertEqual(12.56, areaOfCircle(2))
        self.assertEqual(314, areaOfCircle(10))
        self.assertEqual(94.985, areaOfCircle(5.5))
        self.assertEqual(153.86, areaOfCircle(7))
        

import random,string
class StringTests(PGHS_TestingGame):

    def test_returns_theSameStringDoubled(self):
        # Write a function called returnSameStringDoubled. This function should take a
        # single parameter, a string, and return that string doubled. For example,
        # if the function is called like returnSameStringDoubled("hello")
        # then the return value should be "hellohello"
        r_string = self.randomString(25)
        self.assertEqual(r_string*2,returnSameStringDoubled(r_string))




class NumberTests(PGHS_TestingGame):

    def test_returns_a_number(self):
        self.assertIsInstance(returnsANumber(),int)


    def test_returns_number_squared(self):
        number = 25
        number_squared = number ** 2
        self.assertEqual(number_squared,getNumberSquared(number))


    def test_returns_remainder_of_two_numbers_divided(self):
        number2 = self.random_number(1,101)
        number1 = self.random_number(100,10000)
        remainder = number1 % number2
        self.assertEqual(remainder,getRemainder(number1,number2))

