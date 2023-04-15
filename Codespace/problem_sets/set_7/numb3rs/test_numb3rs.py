# Test program for numb3rs.py



# Imports function to be tested
from numb3rs import validate

# Test definitions
def test_correct_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.10.100.200") == True
    assert validate("140.247.235.144") == True

def test_incorrect_range():
    assert validate("256.256.256.256") == False
    assert validate("7.454.54.9") == False
    assert validate("0.0.0.1000") == False

def test_incorrect_format():
    assert validate("0:0:0:0") == False
    assert validate("0.0") == False

def test_incorrect_input():
    assert validate("cat") == False
    assert validate("a.b.c.d") == False