import unittest
from somemath import absolute_value_class

class TestSomeMath2(unittest.TestCase):
    def test_absolute_value_positive2(self):
        absv = absolute_value_class()
        self.assertEqual(absv.absolute_value(5), 5)
