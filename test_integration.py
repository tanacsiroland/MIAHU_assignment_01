import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_and_multiply_integration(self):
        # This tests the interaction between add() and multiply()
        result = self.calc.add_and_multiply(2, 3, 4)  # (2+3)*4 = 20
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()