from io import StringIO
import unittest
from unittest.mock import patch

from string_formatting.string_formatting import FormattedPrinter


class TestFormattedPrinter(unittest.TestCase):
    def test_print_formatted(self):
        printer = FormattedPrinter(5)
        expected_output = '  1   1   1   1\n  2   2   2  10\n  ' \
                          '3   3   3  11\n  4   4   4 100\n  5   5   5 101\n'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            printer.print_formatted()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_constructor(self):
        printer = FormattedPrinter(10)
        self.assertEqual(printer.number, 10)

    def test_print_single_number(self):
        printer = FormattedPrinter(1)
        expected_output = '1 1 1 1\n'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            printer.print_formatted()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_zero_input(self):
        printer = FormattedPrinter(0)
        expected_output = ''
        with patch('sys.stdout', new=StringIO()) as fake_output:
            printer.print_formatted()
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
