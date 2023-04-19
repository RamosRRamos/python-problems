# https://www.hackerrank.com/challenges/designer-door-mat/problem


class DesignerDoorMat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_rows(self):
        return int(self.x / 2 + 1)


if __name__ == '__main__':
    x, y = map(int, input().split())
    door_mat = DesignerDoorMat(x, y)
    print(door_mat.calculate_rows())
