# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

import textwrap


class Wrapper:

    def __init__(self, string, max_width):
        self.string = string
        self.max_width = max_width

    def wrap_(self):
        """
        This is a method called wrap_ which belongs to a class,
         represented by self. It uses the textwrap module to wrap
         the string attribute of the class instance into lines no
         longer than max_width, and joins them with line breaks ("\n").
         The method then returns the resulting string.
        """
        return "\n".join(textwrap.wrap(self.string, self.max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrapper = Wrapper(string, max_width)
    result = wrapper.wrap_()
    print(result)
