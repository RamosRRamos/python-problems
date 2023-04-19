import sys
from io import StringIO

import pytest

from string_formatting.string_formatting import print_formatted


def test_print_formatted():
    # testing for number = 5
    expected_output = """    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
"""
    with StringIO() as buffer:
        sys.stdout = buffer  # redirect stdout to buffer
        print_formatted(5)
        output = buffer.getvalue()
        assert output == expected_output
    sys.stdout = sys.__stdout__  # restore original stdout

    # testing for number = 0
    expected_output = ""
    with StringIO() as buffer:
        sys.stdout = buffer
        print_formatted(0)
        output = buffer.getvalue()
        assert output == expected_output
    sys.stdout = sys.__stdout__

    # testing for negative number
    with pytest.raises(ValueError):
        print_formatted(-1)
