import pytest
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


def test_ignore_big_num():
    assert add("1001,2,3") == 5
    assert add("1000,2,3") == 1005


def test_negatives():
    with pytest.raises(Exception, match=r"Negatives not allowed: -1"):
        add("-1,2")

    with pytest.raises(Exception, match=r"Negatives not allowed: -4,-5"):
        add("2,-4,3,-5")