class InputCase:
    def __init__(self, x, k, value):
        self.x = x
        self.k = k
        self.value = value

    def evaluate_input(self):
        if self.value == self.k:
            print('True')
        else:
            print('False')


if __name__ == '__main__':
    x, k = map(float, input().strip().split())
    value = eval(input())

    input_case = InputCase(x, k, value)
    input_case.evaluate_input()