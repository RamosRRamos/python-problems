import sys
import unittest
from io import StringIO

from python_exception.python_exception import PythonExceptionCase


class PythonExceptionCaseTest(unittest.TestCase):
    def test_perform_division(self):
        """
        This test sets up a PythonExceptionCase object with a specified
        number of iterations, uses StringIO to redirect input and output,
        invokes the perform_division method of the object, and checks if the
        output matches the expected output. Note that you would need to import
        the PythonExceptionCase class for this test to work.

        :return:
        """
        test_input = '3 0\n10 2\n12 4\n6 0\n'
        expected_output = 'Error Code: ' \
                          'integer division or modulo by zero\n5\n3\n'

        py_exception_case = PythonExceptionCase(3)

        # Redirect stdout to capture output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Redirect stdin to use test input instead of user input
        test_input_stream = StringIO(test_input)
        sys.stdin = test_input_stream

        py_exception_case.perform_division()

        # Reset stdout and stdin
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        self.assertEqual(captured_output.getvalue(), expected_output)
