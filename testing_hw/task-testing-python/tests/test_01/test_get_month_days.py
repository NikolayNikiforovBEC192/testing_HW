from simple_library_01.functions import get_month_days
import pytest

def test_get_month_days():
    assert 30 == get_month_days(1930, 1)
    assert 29 == get_month_days(2024, 2)
    assert 28 == get_month_days(2023, 2)
    assert 31 == get_month_days(2024, 12)
    assert 30 == get_month_days(2024, 6)
    with pytest.raises(AttributeError) as e:
         get_month_days(2024, 25)
    assert 'Month should be in range [1-12]' in str(e)