import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):  # test method must start with test_
        self.assertEqual(calculator.add(10, 5), 15)
        # Lets test edge cases
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-2, -2), -4)

    def test_mul(self):  # test method must start with test_
        self.assertEqual(calculator.mul(10, 5), 50)
        # Lets test edge cases
        self.assertEqual(calculator.mul(-1, 0), 0)
        self.assertEqual(calculator.mul(-2, -2), 4)


if __name__ == '__main__':
    unittest.main()
