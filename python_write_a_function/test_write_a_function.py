import unittest

from python_write_a_function.write_a_function import LeapYearChecker


class TestLeapYearChecker(unittest.TestCase):
    def test_leap_year(self):
        checker = LeapYearChecker(2020)
        self.assertTrue(checker.is_leap())

    def test_non_leap_year(self):
        checker = LeapYearChecker(2021)
        self.assertFalse(checker.is_leap())


if __name__ == '__main__':
    unittest.main()