# Test program for working.py



# Imports function to be tested
import working, pytest

# Test definitions
def test_correct_range():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert working.convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_incorrect_range():
    with pytest.raises(ValueError):
        working.convert("8:60 AM to 4:60 PM")
        working.convert("13:00 AM to 3:00 PM")
        working.convert("3:00 AM to 13:00 PM")

def test_incorrect_format_1():
    with pytest.raises(ValueError):
        working.convert("9AM to 5PM")

def test_incorrect_format_2():
    with pytest.raises(ValueError):
        working.convert("9 AM - 5 PM")

def test_incorrect_format_3():
    with pytest.raises(ValueError):
        working.convert("03:00 to 13:00")

def test_incorrect_input_1():
    with pytest.raises(ValueError):
        working.convert("10:7 AM - 5:1 PM")

def test_incorrect_input_2():
    with pytest.raises(ValueError):
        working.convert("cat")

def test_incorrect_input_3():
    with pytest.raises(ValueError):
        working.convert("a.b.c.d")