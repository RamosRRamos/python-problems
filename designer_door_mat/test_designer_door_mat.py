import io
import unittest
from contextlib import redirect_stdout

from designer_door_mat.designer_door_mat import DesignerDoorMat


class TestDesignerDoorMat(unittest.TestCase):
    def test_create_mat(self):
        door_mat = DesignerDoorMat(7, 21)
        door_mat.create_mat()
        self.assertEqual(len(door_mat.mat), 7)
        self.assertEqual(len(door_mat.mat[0]), 21)

    def test_dashes(self):
        door_mat = DesignerDoorMat(7, 21)
        self.assertEqual(door_mat._dashes(0), '----')
        self.assertEqual(door_mat._dashes(1), '---')
        self.assertEqual(door_mat._dashes(2), '--')
        self.assertEqual(door_mat._dashes(3), '-')

    def test_dots(self):
        door_mat = DesignerDoorMat(7, 21)
        self.assertEqual(door_mat._dots(0), '')
        self.assertEqual(door_mat._dots(1), '.|.')
        self.assertEqual(door_mat._dots(2), '.|..|.')

    def test_print_mat(self):
        n, m = 7, 21
        door_mat = DesignerDoorMat(n, m)
        door_mat.create_mat()

        expected_output = [
            '---------.|.---------',
            '------.|..|..|.------',
            '---.|..|..|..|..|.---',
            '-------WELCOME-------',
            '---.|..|..|..|..|.---',
            '------.|..|..|.------',
            '---------.|.---------'
        ]

        # Use StringIO to capture stdout from print_mat()
        with io.StringIO() as buf, redirect_stdout(buf):
            door_mat.print_mat()
            output = buf.getvalue().split('\n')

        # Check that each line of the output matches the expected output
        for i, line in enumerate(expected_output):
            self.assertEqual(line, output[i])


if __name__ == '__main__':
    unittest.main()
