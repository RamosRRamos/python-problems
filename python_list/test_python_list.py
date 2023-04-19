import io
from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import patch

from python_list.python_list import ListManipulator


class TestListManipulator(TestCase):
    def setUp(self) -> None:
        self.list_manipulator = ListManipulator()

    @patch('builtins.input',
           side_effect=['12', 'insert 0 5', 'insert 1 10', 'insert 0 6',
                        'print', 'remove 6', 'append 9', 'append 1',
                        'sort', 'print', 'pop', 'reverse', 'print'])
    def test_manipulate_list(self, mock_input):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            self.list_manipulator.manipulate_list()
            output = buffer.getvalue().strip()

        expected_output = "['6', '5', '10']\n['5', '6', '10', '9', '1']" \
                          "\n['5', '6', '10', '9']"

        self.assertEqual(output, expected_output)
