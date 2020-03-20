from sample import add


def test_empty_string():
    assert add("") == 0


def test_single_num():
    assert add("1") == 1
    assert add("83") == 83


def test_two_num():
    assert add("4,5") == 9
    assert add("14,3") == 17