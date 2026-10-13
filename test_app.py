from app import add, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(10, 20) == 30


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 5) == 20
    