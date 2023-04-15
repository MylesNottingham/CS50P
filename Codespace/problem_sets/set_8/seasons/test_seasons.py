# Test program for seasons.py



# Imports functions for tests
import seasons, datetime, pytest

# Test definitions
def test_get_birthday():
    assert str(seasons.get_birthday("1989-01-01")) == "1989-01-01"
    assert str(seasons.get_birthday("2020-12-31")) == "2020-12-31"
    with pytest.raises(SystemExit):
        seasons.get_birthday("2020-13-01")
        seasons.get_birthday("2020-01-32")
        seasons.get_birthday("January 1, 2020")

def test_format_time():
    assert seasons.format_time(datetime.timedelta(days=365)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.format_time(datetime.timedelta(days=1)) == "One thousand, four hundred forty minutes"
    assert seasons.format_time(datetime.timedelta(days=10)) == "Fourteen thousand, four hundred minutes"