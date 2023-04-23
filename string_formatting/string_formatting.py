# https://www.hackerrank.com/challenges/python-string-formatting/problem


class FormattedPrinter:
    def __init__(self, number):
        """
        Initializes a new instance of the FormattedPrinter class.
         Args:
             number (int): The maximum number to print formatted numbers up to.
        """
        self.number = number

    def print_formatted(self):
        """
        Prints formatted numbers from 1 to the maximum number specified in
        the constructor.
        The numbers are printed out in columns, with each column containing the
        decimal, octal, hexadecimal, and binary representation of a number.
        Each column is right-justified to the width of the
        maximum number specified in the constructor.
        """
        w = len(bin(self.number)[2:])
        for i in range(self.number):
            i += 1
            print(f'{str(i).rjust(w)} {oct(i)[2:].rjust(w)} '
                  f'{hex(i)[2:].upper().rjust(w)} {bin(i)[2:].rjust(w)}')


if __name__ == '__main__':
    n = int(input())
    printer = FormattedPrinter(n)
    printer.print_formatted()
