# Test program for plates.py



# Imports function from module for test
from plates import is_valid

# Test definitions
def test_is_between_two_and_six():
    assert is_valid("XXXX") == True
    assert is_valid("X") == False
    assert is_valid("XXXXXXXX") == False

def test_first_two_alpha():
    assert is_valid("XX99") == True
    assert is_valid("9999") == False

def test_alphanumeric_only():
    assert is_valid("XX99") == True
    assert is_valid("XX-XX") == False
    assert is_valid("XX99:)") == False

def test_number_check():
    assert is_valid("XX99") == True
    assert is_valid("XX99XX") == False
    assert is_valid("XX0099") == False