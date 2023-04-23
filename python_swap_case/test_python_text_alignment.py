from python_swap_case.python_swap_case import StringManipulation


def test_swap_case():
    # Test basic functionality
    s = StringManipulation('Hello, world!')
    assert s.swap_case() == 'hELLO, WORLD!'

    # Test empty string
    s = StringManipulation('')
    assert s.swap_case() == ''

    # Test string with only one character
    s = StringManipulation('A')
    assert s.swap_case() == 'a'

    # Test string with only non-alphabetic characters
    s = StringManipulation('123!@#')
    assert s.swap_case() == '123!@#'

    # Test string with only lowercase characters
    s = StringManipulation('hello')
    assert s.swap_case() == 'HELLO'

    # Test string with only uppercase characters
    s = StringManipulation('HELLO')
    assert s.swap_case() == 'hello'

    # Test string with mixed case and non-alphabetic characters
    s = StringManipulation('HeLLo, WoRLd123!@#')
    assert s.swap_case() == 'hEllO, wOrlD123!@#'