import unittest
from calculator import Calculator
from typing import assert_type

class TestCalculatorUnit(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_show_info(self):
        test_info = self.calc.show_info()
        assert_type(test_info, str)

if __name__ == '__main__':
    unittest.main()