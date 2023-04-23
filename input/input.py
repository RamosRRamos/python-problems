"""
https://www.hackerrank.com/challenges/input/
input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
Task

You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k . Your task is to verify if P(x) = K.

Constraints
All coefficients of polynomial P are integers.
x and y are also integers.

Input Format

The first line contains the space separated values of x and k .
The second line contains the polynomial P.

Output Format

Print True if P(x) = k. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True

Explanation

P(1) = 1^3 + 1^2 + 1 + 1 =  4 = k

Hence, the output is True.

"""


class InputCase:
    def __init__(self, x, k, value):
        self.x = x
        self.k = k
        self.value = eval(value)

    def evaluate_input(self) -> bool:
        """
        This is a method named evaluate_input belonging to a class.
        It checks if the value of an instance variable value is equal
        to another instance variable k. If they are equal, it returns True,
        otherwise it returns False.
        :return: boolean
        """
        print(self.value == self.k)
        return self.value == self.k

if __name__ == '__main__':
    x, k = map(float, input().strip().split())
    value = input()

    input_case = InputCase(x, k, value)
    input_case.evaluate_input()
