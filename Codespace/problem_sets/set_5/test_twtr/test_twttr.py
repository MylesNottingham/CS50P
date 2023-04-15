# Test program for twttr.py



# Imports function to be tested
from twttr import shorten

# Test definitions
def test_upper():
    assert shorten("1A2E3I4O5U") == "12345"
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_lower():
    assert shorten("1a2e3i4o5u") == "12345"
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_mixed():
    assert shorten("SpOnGeBoB") == "SpnGBB"

def test_mixed_double():
    assert shorten("SpOnGeBoB sQuArEpAnTs") == "SpnGBB sQrpnTs"

def test_punctuation():
    assert shorten("Bond, James Bond") == "Bnd, Jms Bnd"