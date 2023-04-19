# URL: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

# LIST #

def insert(data: list, args) -> list:
    data.insert(int(args[0]), int(args[1]))
    return data


def print_f(data: list, args):
    print(data)
    return data


def remove(data: list, args) -> list:
    data.remove(int(args[0]))
    return data


def append(data: list, args):
    data.append(int(args[0]))
    return data


def sort(data: list, args):
    data.sort()
    return data


def pop(data: list, args):
    data.pop()
    return data


def reverse(data: list, args) -> list:
    data.reverse()
    return data


def selector(selector: str, data: list, args):
    selectors = {
        'insert': insert,
        'remove': remove,
        'append': append,
        'sort': sort,
        'pop': pop,
        'reverse': reverse,
        'print': print_f
    }

    return selectors[selector](data, args)


def get_list(input_: str):
    split = input_.split(' ')
    return {'index': split[0], 'split': split[1:3:]}


if __name__ == '__main__':
    data_list = []
    N = int(input())
    for i in range(N):
        re = get_list(input())
        data_list = selector(re['index'], data_list, re['split'])
