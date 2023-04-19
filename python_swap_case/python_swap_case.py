# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s: str):
    d = []
    c = 0
    for i in s:
        if i.isupper():
            d.append(s[c].lower())
        else:
            d.append(s[c].upper())
        c = c+1
    return "".join(d)


if __name__ == '__main__':
    n = input()
    result = swap_case(n)
    print(result)
