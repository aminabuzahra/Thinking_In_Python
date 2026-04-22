import unittest
import calculator

# Unit Testing terminology:
# Test Case فحص حالة واحدة فقط
# Test Suite فحص عدة حالات في آن واحد
# Test Runner: الفاحص
# Test ......: المفحوص
# ...........: Preparing and releasing

class TestMyCalculator(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(calculator.add(5,3), 8)

