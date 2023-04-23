# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# EXCEPTION #


class PythonExceptionCase:
    def __init__(self, t):
        self.t = t

    def perform_division(self):
        """
        This is a method written in
        Python that performs division operations.
        It takes input from the user and splits it into two integers for
        integer division. If a ZeroDivisionError or ValueError occurs
        during the division operation, it prints an error code message.
        The method is part of a class and uses the 'self' parameter
        to access the class variables.
        :return:
        """
        for i in range(self.t):
            try:
                x = input().split()
                print(int(x[0]) // int(x[1]))
            except ZeroDivisionError as e:
                print("Error Code:", e)
            except ValueError as e:
                print("Error Code:", e)



if __name__ == '__main__':
    t = int(input())
    py_exception_case = PythonExceptionCase(t)
    py_exception_case.perform_division()
