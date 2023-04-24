# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

class StringManipulator:

    def __init__(self, line_):
        # initialize any class variables here
        self.line = line_

    def split_and_join(self):
        """
        This is a method called split_and_join. It receives self parameter,
        which refers to an instance of a class. The method first splits the
        line attribute into a list of words using the split() method,
        and then  returns a string made by joining the words with a hyphen
        using the join() method.
        """
        self.line = self.line.split()
        return "-".join(self.line)


if __name__ == '__main__':
    # example usage
    line = input("Enter a line to split and join: ")
    sm = StringManipulator(line)
    result = sm.split_and_join()
    print(result)
