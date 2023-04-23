# https://www.hackerrank.com/challenges/designer-door-mat/problem


class DesignerDoorMat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_rows(self):
        """
        This is a method written in Python that calculates the number
        of rows needed to display some content based on the width represented
        by self.x. The method takes no arguments other than the instance of
        the class it belongs to (indicated by the use of self).
        It returns an integer value representing the number of rows needed
        for the display.

        :return:
        """
        return int(self.x / 2 + 1)


if __name__ == '__main__':
    x, y = map(int, input().split())
    door_mat = DesignerDoorMat(x, y)
    print(door_mat.calculate_rows())
