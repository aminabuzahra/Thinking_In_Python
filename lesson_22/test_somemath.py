import unittest
from somemath import absolute_value_class

class TestSomeMath(unittest.TestCase):
    def test_absolute_value_positive(self):
        absv = absolute_value_class()
        self.assertEqual(absv.absolute_value(5), 5)  # add assertion here
    def test_absolute_value_negative(self):
        absv = absolute_value_class()
        self.assertEqual(absv.absolute_value(-5), 5)  # add assertion here
    def test_absolute_value_zero(self):
        absv = absolute_value_class()
        self.assertEqual(absv.absolute_value(0), 0)  # add assertion here





