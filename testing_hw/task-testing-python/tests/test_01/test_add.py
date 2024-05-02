from simple_library_01.functions import add


def test_add():
    assert 4 == add(2, 2)
    assert 0 == add(-1, 1)
    assert 3 == add(1, 2)
    assert 3 == add(2, 1)

