import unittest

from src.calculator import suma, resta, multi

class CalculatorTest(unittest.TestCase):
   
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

    def test_multi(self):
        self.assertEqual(multi(10, 5), 50)