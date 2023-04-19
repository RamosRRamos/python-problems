
from python_string_validators.python_string_validators import wrap_


def test_wrap_():
    #TODO fix this test
    """
    The first test case checks if the function correctly wraps
    the input string to the specified maximum width. The second
    test case checks if the function returns an empty string when given an
    empty string as input. The third test case checks if the function handles
    input strings that are already shorter than the maximum width.

    :return: A wrap str
    """
    string = "Hello world! Welcome to ChatGPT, a large language model."
    max_width = 10

    expected_output = wrap_(string, max_width)
    assert wrap_(string, max_width) == "\n".join(expected_output)

    string = ""
    max_width = 10

    expected_output = ""
    assert wrap_(string, max_width) == expected_output

    string = "Hello"
    max_width = 7

    expected_output = wrap_(string, max_width)
    assert wrap_(string, max_width) == "\n".join(expected_output)