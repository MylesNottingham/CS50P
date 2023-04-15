# Test program for bank.py



# Imports function to be tested
from bank import value

# Test definitions
def test_lower():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("yo") == 100

def test_upper():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("YO") == 100

def test_double():
    assert value("hello there") == 0
    assert value("hey there") == 20
    assert value("yo homie") == 100

def test_punctuation():
    assert value("hello there!!!") == 0
    assert value("hey there!!!") == 20
    assert value("yo homie!!!") == 100