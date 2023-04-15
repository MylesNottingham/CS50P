# Test program for um.py



# Imports function to be tested
from um import count

# Test definitions
def test_single_um():
    assert count("um") == 1

def test_double_um():
    assert count("um um") == 2

def test_word_with_um():
    assert count("bubblegum") == 0

def test_sentence_with_ums():
    assert count("Um, like, I think, umm, dum, um, I may be, um, getting it.") == 3