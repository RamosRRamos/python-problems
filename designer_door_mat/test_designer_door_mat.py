import unittest
from io import StringIO
import sys

from designer_door_mat.designer_door_mat import DesignerDoorMat


class DesignerDoorMatTest(unittest.TestCase):
    def test_calculate_rows(self):
        test_input = '9 27\n'
        expected_output = '5\n'

        x, y = map(int, test_input.split())
        door_mat = DesignerDoorMat(x, y)

        # Redirect stdout to capture output
        captured_output = StringIO()
        sys.stdout = captured_output

        print(door_mat.calculate_rows())

        # Reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)
