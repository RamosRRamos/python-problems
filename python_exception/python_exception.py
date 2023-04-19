# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# EXCEPTION #


class PythonExceptionCase:
    def __init__(self, t):
        self.t = t

    def perform_division(self):
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
