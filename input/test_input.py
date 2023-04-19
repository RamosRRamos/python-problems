import unittest
from io import StringIO
import sys

from input.input import InputCase


class InputCaseTest(unittest.TestCase):
    def test_evaluate_input(self):
        test_input = '2 3\n2 + 3j\n'
        expected_output = 'True\n'

        x, k = map(float, test_input.strip().split()[:2])
        value = eval(test_input.strip().split()[2])
        input_case = InputCase(x, k, value)

        # Redirect stdout to capture output
        captured_output = StringIO()
        sys.stdout = captured_output

        input_case.evaluate_input()

        # Reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)
