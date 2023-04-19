# URL:
# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

# LIST #

class ListManipulator:
    def __init__(self):
        self.data_list = []

    def insert(self, args: list) -> None:
        self.data_list.insert(int(args[0]), int(args[1]))

    def print_f(self) -> None:
        print(self.data_list)

    def remove(self, args: list) -> None:
        self.data_list.remove(int(args[0]))

    def append(self, args: list) -> None:
        self.data_list.append(int(args[0]))

    def sort(self) -> None:
        self.data_list.sort()

    def pop(self) -> None:
        self.data_list.pop()

    def reverse(self) -> None:
        self.data_list.reverse()

    def selector(self, selector: str, args: list) -> None:
        selectors = {
            'insert': self.insert,
            'remove': self.remove,
            'append': self.append,
            'sort': self.sort,
            'pop': self.pop,
            'reverse': self.reverse,
            'print': self.print_f
        }
        selectors[selector](args)

    def get_list(self, input_: str) -> dict:
        split = input_.split(' ')
        return {'index': split[0], 'split': split[1:3:]}

    def manipulate_list(self) -> None:
        N = int(input())
        for i in range(N):
            re = self.get_list(input())
            self.selector(re['index'], re['split'])


if __name__ == '__main__':

    if __name__ == '__main__':
        list_manipulator = ListManipulator()
        list_manipulator.manipulate_list()
