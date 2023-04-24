from python_string_validators.python_string_validators import Wrapper


def test_wrap_():
    # Case 1: Short string, long max_width
    w = Wrapper("hello", 10)
    assert w.wrap_() == "hello"

    # Case 2: String length = max_width
    w = Wrapper("hi there", 8)
    assert w.wrap_() == "hi there"

    # Case 3: String with newlines
    w = Wrapper("hello\nworld", 5)
    assert w.wrap_() == "hello\nworld"
