class DesignerDoorMat:
    def __init__(self, n, m):
        """
        Creates a new instance of DesignerDoorMat with the specified dimensions.

        Args:
        - n (int): number of rows in the mat
        - m (int): number of columns in the mat
        """
        self.n = n
        self.m = m

    def create_mat(self):
        """
        Creates the door mat based on the dimensions specified in __init__.
        The three components of the mat (top half, middle row, and bottom half)
        are created separately and concatenated
        into a list that represents the complete mat. The resulting list is
        stored in `self.mat`.
        """
        top_half = self._create_top_half()
        middle_row = self._create_middle_row()
        bottom_half = self._create_bottom_half()
        self.mat = top_half + [middle_row] + bottom_half

    def print_mat(self):
        """
        Prints the door mat to stdout, line by line.
        """
        for line in self.mat:
            print(line)

    def _create_top_half(self):
        """
        Creates the top half of the door mat.

        Returns:
        - A list of strings representing the lines of the top half of the mat.
        """
        lines = []
        for i in range(self.n // 2):
            dashes = self._dashes(i)
            dots = self._dots(i)
            lines.append(dashes + dots + dashes)
        return lines

    def _create_middle_row(self):
        """
        Creates the middle row of the door mat.

        Returns:
        - A string representing the middle row of the mat.
        """
        welcome_width = 7
        width = (self.m - welcome_width) // 2
        return "-" * width + "WELCOME" + "-" * width

    def _create_bottom_half(self):
        """
        Creates the bottom half of the door mat.

        Returns:
        - A list of strings representing the lines of the bottom half of the mat.
        """
        lines = []
        for i in range(self.n // 2 - 1, -1, -1):
            dashes = self._dashes(i)
            dots = self._dots(i)
            lines.append(dashes + dots + dashes)
        return lines

    def _dashes(self, i):
        """
        Creates a string of "-" characters for the specified number of columns.

        Args:
        - i (int): number of dashes (width) desired

        Returns:
        - A string containing `i` "-" characters
        """
        width = (self.m - 3 * (i * 2 + 1)) // 2
        return "-" * width

    def _dots(self, i):
        """
        Creates a string of ".|." characters for the specified number of columns.

        Args:
        - i (int): number of dot-pipe sets (width) desired

        Returns:
        - A string containing `i` sets of dot-pipe (".|."), each separated by
        a space character.
        """
        dots = ".|." * (i * 2 + 1)
        return dots


if __name__ == '__main__':
    n, m = map(int, input().split())
    door_mat = DesignerDoorMat(n, m)
    door_mat.create_mat()
    door_mat.print_mat()
