# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

class StringManipulation:
    def __init__(self, s):
        self.s = s

    def swap_case(self):
        """
        This is a method in Python which belongs to a class and is defined as
        swap_case(). It takes no arguments except self
        (which refers to the instance of the class that calls this method)
        and returns a string.
        This method iterates through each character of the string s,
        and if a character is uppercase, it converts it to lowercase
        and appends it to the list d. If the character is lowercase,
        it converts it to uppercase and appends it to the same list.
        Finally, it joins all the characters in the list d to form a string.
        The purpose of this method is to swap the case of every letter in a
        given string.
        """
        d = []
        c = 0
        for i in self.s:
            if i.isupper():
                d.append(self.s[c].lower())
            else:
                d.append(self.s[c].upper())
            c = c + 1
        return "".join(d)


if __name__ == '__main__':
    n = input("Enter a string: ")
    obj = StringManipulation(n)
    result = obj.swap_case()
    print(result)
