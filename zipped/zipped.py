# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import List


class StudentStatistics:
    """
    A class to calculate the average of each column of a matrix of students'
    grades.

    Attributes
    ----------
    lines : int
        The number of rows in the matrix.
    column : int
        The number of columns in the matrix.
    students : List[List[float]]
        A list of lists containing the grades of the students.

    Methods
    -------
    from_input() -> StudentStatistics:
        Reads input from standard input and returns an instance of the class.
    calculate_average() -> None:
        Calculates the average of each column of the matrix and prints it to
        standard output.
    """

    def __init__(self, lines: int, column: int, students: List[List[float]]):
        """
        Initializes a new instance of the class.

        Attributes
        ----------
        lines : int
            The number of rows in the matrix.
        column : int
            The number of columns in the matrix.
        students : List[List[float]]
            A list of lists containing the grades of the students.
        """
        self.lines = lines
        self.column = column
        self.students = students

    @classmethod
    def from_input(cls) -> "StudentStatistics":
        """
        Reads input from standard input and returns an instance of the class.

        Returns
        -------
        StudentStatistics
            A new instance of the class.
        """
        x = input()
        lines, column = int(x.split(" ")[0]), int(x.split(" ")[1])

        students = []
        for t in range(column):
            students.append(input())

        for t in range(len(students)):
            students[t] = students[t].split()
            for x in range(len(students[t])):
                students[t][x] = float(students[t][x])

        return cls(lines=lines, column=column, students=students)

    def calculate_average(self) -> None:
        """
        Calculates the average of each column of the matrix and prints it to
        standard output.
        """
        student_zip = list(zip(*self.students))

        for student in student_zip:
            value = sum(student) / self.column
            print(value)


if __name__ == "__main__":
    s = StudentStatistics.from_input()
    s.calculate_average()
