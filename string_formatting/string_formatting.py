# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true


def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(number):
        i += 1
        print(
            f'{str(i).rjust(w)} {oct(i)[2:].rjust(w)} {hex(i)[2:].upper().rjust(w)} {bin(i)[2:].rjust(w)}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
