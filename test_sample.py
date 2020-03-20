from sample import add


def test_empty_string():
    assert add("") == 0


def test_single_num():
    assert add("1") == 1
    assert add("83") == 83