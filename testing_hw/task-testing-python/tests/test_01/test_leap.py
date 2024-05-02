from simple_library_01.functions import is_leap
import pytest

def test_is_leap():
    with pytest.raises(AttributeError) as e:
        is_leap(-20)
    assert 'Year must be greater than 0' in str(e)
    assert False == is_leap(3)
    assert True == is_leap(400)
    assert False == is_leap(200)
    


