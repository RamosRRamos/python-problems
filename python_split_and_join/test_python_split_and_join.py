import unittest

from python_split_and_join.python_split_and_join import split_and_join


class TestSplitAndJoin(unittest.TestCase):

    def test_split_and_join(self):
        """
               Here, we import the split_and_join() function from a separate file called split_and_join.py.
               Then, we write a unittest test case called TestSplitAndJoin which inherits from unittest.TestCase.
               Within the test case, we define a test method called test_split_and_join() which includes
               two assertions that verify if the function returns the expected output for the given inputs.
               Finally, we use unittest.main() to run the tests.

           """
        self.assertEqual(split_and_join("Hello World"), "Hello-World")
        self.assertEqual(split_and_join("This is a sentence."),
                         "This-is-a-sentence.")


if __name__ == '__main__':
    unittest.main()
