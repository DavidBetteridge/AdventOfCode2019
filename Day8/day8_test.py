import Day8.day8 as day

def test_day_8_part_one():
    assert day.part_one() == 1215

def test_day_8_part_two():
    lines = day.part_two().splitlines()

    assert lines[0] == '1    1  1  11  111  1  1 '
    assert lines[1] == '1    1  1 1  1 1  1 1  1 '
    assert lines[2] == '1    1111 1    1  1 1111 '
    assert lines[3] == '1    1  1 1    111  1  1 '
    assert lines[4] == '1    1  1 1  1 1    1  1 ' 
    assert lines[5] == '1111 1  1  11  1    1  1 '