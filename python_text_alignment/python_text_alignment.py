# https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

class TextAlignment:
    def __init__(self, thickness: int, character: str):
        self.thickness = thickness
        self.character = character

    def create(self):
        # Top Cone
        for i in range(self.thickness):
            print((self.character * i).rjust(
                self.thickness - 1) + self.character + (
                              self.character * i).ljust(self.thickness - 1))

        # Top Pillars
        for i in range(self.thickness + 1):
            print(
                (self.character * self.thickness).center(self.thickness * 2) + (
                            self.character * self.thickness).center(
                    self.thickness * 6))

        # Middle Belt
        for i in range((self.thickness + 1) // 2):
            print((self.character * self.thickness * 5).center(
                self.thickness * 6))

        # Bottom Pillars
        for i in range(self.thickness + 1):
            print(
                (self.character * self.thickness).center(self.thickness * 2) + (
                            self.character * self.thickness).center(
                    self.thickness * 6))

        # Bottom Cone
        for i in range(self.thickness):
            print(((self.character * (self.thickness - i - 1)).rjust(
                self.thickness) + self.character + (
                               self.character * (self.thickness - i - 1)).ljust(
                self.thickness)).rjust(self.thickness * 6))


if __name__ == '__main__':
    # Replace all ______ with rjust, ljust or center.

    thickness = int(input())  # This must be an odd number
    text_align = TextAlignment(thickness, 'H')
    text_align.create()
