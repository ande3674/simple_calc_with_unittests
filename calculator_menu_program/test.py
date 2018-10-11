from calculator_menu_program import menu, functions
import unittest
from unittest.mock import patch

class MyTest(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(functions.add(1, 2), 3)
        self.assertEqual(functions.add(-1, 2), 1)
        self.assertEqual(functions.add(-10, -2), -12)
        self.assertEqual(functions.add(8, -3), 5)
        self.assertEqual(functions.add(.5, 3.2), 3.7)

    def test_subtract_function(self):
        self.assertEqual(functions.subtract(1, 2), -1)
        self.assertEqual(functions.subtract(-10, 3), -13)
        self.assertEqual(functions.subtract(-5, -6), 1)
        self.assertEqual(functions.subtract(7, -12), 19)
        self.assertEqual(functions.subtract(4.8, 2.3), 2.5)

    def test_multiply_function(self):
        self.assertEqual(functions.multiply(10, 3), 30)
        self.assertEqual(functions.multiply(-1, 6), -6)
        self.assertEqual(functions.multiply(-4, -7), 28)
        self.assertEqual(functions.multiply(5, -5), -25)
        self.assertEqual(functions.multiply(.25, 16.5), 4.125)

    def test_divide_function(self):
        self.assertEqual(functions.divide(10, 5), 2)
        self.assertEqual(functions.divide(-1, 4), -0.25)
        self.assertEqual(functions.divide(-4, -8), 0.5)
        self.assertEqual(functions.divide(5, -5), -1)
        self.assertEqual(functions.divide(5, -0.5), -10.0)
        self.assertEqual(functions.divide(0, 100), 0)
        with self.assertRaises(ZeroDivisionError):
            functions.divide(4, 0)

    def test_modulus_function(self):
        self.assertEqual(functions.modulus(10, 3), 1)
        self.assertEqual(functions.modulus(-10, 6), 2)
        self.assertEqual(functions.modulus(-14, -4), -2)
        self.assertEqual(functions.modulus(25, -3), -2)

    def test_exponent_function(self):
        self.assertEqual(functions.exponent(10, 3), 1000)
        self.assertEqual(functions.exponent(-1, 6), 1)
        self.assertEqual(functions.exponent(-4, -2), 0.0625)
        self.assertEqual(functions.exponent(5, -5), 0.00032)
        self.assertEqual(functions.exponent(0.5, 3), 0.125)

    @patch('menu.get_choice')
    def test_get_choice(self, mock_input):
        mock_input.return_value = 3