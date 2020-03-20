from sample import add


def test_empty_string():
    assert add("") == 0


def test_single_num():
    assert add("1") == 1
    assert add("83") == 83


def test_two_num():
    assert add("4,5") == 9
    assert add("14,3") == 17


def test_multiple_num():
    assert add("1,2,3,4,5") == 15
    assert add("1,1,1,1,1") == 5


def test_newline_delimeter():
    assert add("1\n2,3,4,5") == 15
    assert add("4\n3\n2,1") == 10