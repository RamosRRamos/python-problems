from zipped.zipped import StudentStatistics



def test_calculate_average(capsys):
    students = [[10.0, 20.0, 15.0], [30.0, 40.0, 35.0], [50.0, 60.0, 55.0]]
    s = StudentStatistics(lines=3, column=3, students=students)
    s.calculate_average()
    captured = capsys.readouterr()
    assert captured.out == "30.0\n40.0\n35.0\n"