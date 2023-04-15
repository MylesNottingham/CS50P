# Test program for fuel.py



# Imports modules for test
import fuel, pytest

# Test definitions
def test_convert():
    assert fuel.convert("0/1") == 0
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/3") == 100

def test_convert_value_error():
    with pytest.raises(ValueError):
        fuel.convert("4/2"),
        fuel.convert("A/5")

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"