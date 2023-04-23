import unittest

from input.input import InputCase


class TestInputCase(unittest.TestCase):

    def test_evaluate_input(self):
        # Test case 1
        input_case = InputCase(1, 4, 'x**3 + x**2 + x + 1')
        self.assertTrue(input_case.evaluate_input())

        # Test case 2
        input_case = InputCase(2, 10, '2*x**2 + 2*x + 2')
        self.assertFalse(input_case.evaluate_input())

        # Test case 3
        input_case = InputCase(-1, 15, '-x**2 + 16')
        self.assertTrue(input_case.evaluate_input())

if __name__ == '__main__':
    unittest.main()