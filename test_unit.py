import unittest
from calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

if __name__ == '__main__':
    unittest.main()