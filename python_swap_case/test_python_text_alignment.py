from python_swap_case.python_swap_case import swap_case


def test_swap_case():
    """
    These tests cover:
    A basic example ("Hello World")
    A case with no letters ("123")
    An empty string
    A more complex example with mixed case ("hElLo wOrLd")
    An example with all uppercase ("AbCdEfG")
    A longer example with various characters, including spaces and punctuation.

    :return: return a string with a swap to upper for lower and lower for upper
    """
    assert swap_case("Hello World") == "hELLO wORLD"
    assert swap_case("123") == "123"
    assert swap_case("") == ""
    assert swap_case("hElLo wOrLd") == "HeLlO WoRlD"
    assert swap_case("AbCdEfG") == "aBcDeFg"
    assert swap_case("This is a long string with spaces and punctuation!@#$%^&*()_-+=") == "tHIS IS A LONG STRING WITH SPACES AND PUNCTUATION!@#$%^&*()_-+="
