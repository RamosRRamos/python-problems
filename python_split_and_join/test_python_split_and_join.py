from python_split_and_join.python_split_and_join import StringManipulator


def test_split_and_join():
    # test that split_and_join returns a string
    sm = StringManipulator("hello world")
    result = sm.split_and_join()
    assert isinstance(result, str)

    # test that split_and_join splits and joins the input string correctly
    sm = StringManipulator("hello world")
    result = sm.split_and_join()
    assert result == "hello-world"

    sm = StringManipulator("the quick brown fox jumps over the lazy dog")
    result = sm.split_and_join()
    assert result == "the-quick-brown-fox-jumps-over-the-lazy-dog"
