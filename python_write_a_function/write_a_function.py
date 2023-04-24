class LeapYearChecker:
    def __init__(self, year):
        self.year = year

    def is_leap(self):
        return self.year % 4 == 0 and (
                self.year % 100 != 0 or self.year % 400 == 0)


if __name__ == '__main__':
    checker = LeapYearChecker(2020)
    print(checker.is_leap())
