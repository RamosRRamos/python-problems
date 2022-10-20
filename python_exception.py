# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# EXCEPTION #




if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        try:
            x = input().split()
            print(int(x[0]) // int(x[1]))
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)


