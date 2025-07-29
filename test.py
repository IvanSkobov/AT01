import unittest
from main import safe_modulo

class TestSafeModulo(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(safe_modulo(10, 3), 1)
        self.assertEqual(safe_modulo(20, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(safe_modulo(-10, 3), -1)
        self.assertEqual(safe_modulo(10, -3), 1)
        self.assertEqual(safe_modulo(-10, -3), -1)

    def test_zero_dividend(self):
        self.assertEqual(safe_modulo(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_modulo(10, 0)
        with self.assertRaises(ZeroDivisionError):
            safe_modulo(0, 0)

if __name__ == "__main__":
    unittest.main()