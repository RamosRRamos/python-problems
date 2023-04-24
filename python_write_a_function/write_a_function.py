class LeapYearChecker:
    def __init__(self, year):
        self.year = year

    def is_leap(self):
        """
        This is a method called is_leap defined within a class.
        It checks if the year attribute of the class instance is a
        leap year or not by returning True if it is divisible by 4
        and not divisible by 100 unless it is also divisible by 400.
        :return:
        """
        return self.year % 4 == 0 and (
                self.year % 100 != 0 or self.year % 400 == 0)


if __name__ == '__main__':
    checker = LeapYearChecker(2020)
    print(checker.is_leap())
