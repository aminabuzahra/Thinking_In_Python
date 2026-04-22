import unittest
from calculator2 import Calculator2

class TestCalculatorCase (unittest.TestCase):

    def test_factorial_normal_number(self):

        self.assertEqual(Calculator2.factorial(5), 120)
        self.assertEqual(Calculator2.factorial(7), 5040)

    def test_factorial_1_number(self):
        self.assertEqual(Calculator2.factorial(1), 1)

    def test_factorial_0_number(self):
        self.assertEqual(Calculator2.factorial(0), 1)

    def test_pi(self):
        self.assertAlmostEqual(Calculator2.pi(), 3.1428571)

