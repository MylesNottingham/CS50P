# Test program for jar.py



# Imports functions to be tested
from jar import Jar
import pytest


# Initialization test
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(6)
    assert jar.capacity == 6
    jar = Jar(24)
    assert jar.capacity == 24
    with pytest.raises(ValueError):
            jar = Jar(-2)
            jar = Jar("f")

# String test
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

# Deposit test
def test_deposit():
    jar = Jar()
    jar.deposit(0)
    assert jar.size == 0
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12
    with pytest.raises(ValueError):
            jar = Jar()
            jar.deposit(13)
            jar = Jar(6)
            jar.deposit(7)

# Withdraw test
def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(6)
    assert jar.size == 0
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
            jar = Jar()
            jar.withdraw(1)
            jar = Jar()
            jar.deposit(5)
            jar.withdraw(6)