# Test program for project.py



# Imports functions for tests
import project, pytest


# Test definitions
def test_select_word_length():
    assert project.select_word_length(3) == 3
    assert project.select_word_length(5) == 5
    assert project.select_word_length(10) == 10
    with pytest.raises(OSError):
        project.select_word_length(1)
        project.select_word_length("x")
        project.select_word_length(25)


def test_select_number_of_guesses():
    assert project.select_number_of_guesses(5) == 5
    assert project.select_number_of_guesses(13) == 13
    assert project.select_number_of_guesses(25) == 25
    with pytest.raises(OSError):
        project.select_number_of_guesses(1)
        project.select_number_of_guesses("x")
        project.select_number_of_guesses(30)


def test_list_of_letters():
    assert project.list_of_letters("BOB") == ["B", "O", "B"]
    assert project.list_of_letters("ALEXANDRIA") == ["A", "L", "E", "X", "A", "N", "D", "R", "I", "A"]
    assert project.list_of_letters("PYTHON") == ["P", "Y", "T", "H", "O", "N"]


def test_generate_answer_word():
    assert project.generate_answer_word(["B", "L", "E", "E", "D"], ["C", "R", "E", "E", "D"]) == "**EED"
    assert project.generate_answer_word(["B", "O", "B"], ["A", "L", "E"]) == "***"
    assert project.generate_answer_word(["P", "Y", "T", "H", "O", "N"], ["P", "Y", "T", "H", "O", "N"]) == "PYTHON"