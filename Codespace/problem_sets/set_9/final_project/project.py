# Purdle



# Imports libraries for program
import random, inflect
from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()
p = inflect.engine()


# Starts a word guessing game based on user input and displays that word and definition when the game is over
def main():
    print(intro())
    word_length = select_word_length(input(how_many_letters()))
    number_of_guesses = select_number_of_guesses(input(how_many_guesses()))
    word, upper_words = generate_words(word_length)
    if guessing_game(word, word_length, upper_words, number_of_guesses):
        print(f'"{word}"\nDefinition{english_dict[word]}\n')


def intro():
    return(
        "\n\n\nWelcome to Purdle!\n\n"
        "This is my Wordle inspired command-line game in Python for CS50P\n\n"

        "This program will randomly generate a secret word based on the number of letters you specify between three and ten\n"
        "You will then choose the number of attempts you may have to guess the secret word between five and ten\n\n"

        "When prompted, type your guess. Case does not matter.\n\n"

        "If you guess correctly, you win the game.\n"
        "If you guess incorrectly, your guess will be displayed above a semi-redacted version of the secret word.\n\n"

        "Your guesses are processed on a letter-by-letter basis.\n"
        "If you guess a correct letter in the correct location it will be visible.\n"
        "All other letters will be represented by an '*'.\n"
        "Each subsequent guess will be added to the stack.\n\n"

        "If you guess a correct letter, regardless of its location in the word, it will be listed below this stack.\n"
        "It will also let you know if none of the letters in your guess are in the secret word.\n\n"

        "When the game is over, win or lose, you will see the secret word and the definition.\n\n"

        "Enjoy\n"
    )


# Here to clean up main()
def how_many_letters():
    return "\nHow many letters long would you like your word to be?(3-10) "


# Here to clean up main()
def how_many_guesses():
    return "\nHow many guesses do you think you need?(5-10) "


# Loop prompting user for length of word desired with error checking
def select_word_length(user_input):
    while True:
        try:
            length = int(user_input)
            if length > 2 and length < 11:
                return length
            else:
                raise
        except:
            user_input = input(how_many_letters())


# Loop prompting user for number of guesses desired with error checking
def select_number_of_guesses(user_input):
    while True:
        try:
            number = int(user_input)
            if number > 4 and number < 11:
                return number
            else:
                raise
        except:
            user_input = input(how_many_guesses())


# Generates a list of uppercase words and pickes a random word from the dictionary based on the number of letters specified
def generate_words(word_length):
    english_words = list(english_dict)
    words = list(filter(lambda w: len(w) == word_length, english_words))
    upper_words = []
    for word in words:
        upper_words.append(word.upper())
    return random.choice(words), upper_words



# Guessing game that allows user to guess a secret word based on user defined parameters
def guessing_game(word, word_length, upper_words, number_of_guesses):
    # Establishes some baseline variables and informs user that thier game is starting
    word = word.upper()
    guess_number = 0
    list_of_guesses = []
    list_of_letters_in_word = []
    list_of_letters_not_in_word = []
    print("\n\nThe magic word has been generated")

    # Loop that prompts user for their guess until they get it right or run out of guesses and then returns "True"
    while  number_of_guesses > 0:
        print(f"\nYou have {p.number_to_words(number_of_guesses)} {p.plural('guess', number_of_guesses)} remaining\n")
        guess = guess_is_valid(input("\nGuess the magic word: "), word_length, upper_words)
        if guess == word:
            print("\n\n\n**********     You Win!     **********\n\n\nThe magic word is ", end="")
            return True
        else:
            number_of_guesses = number_of_guesses - 1
            guess_number = guess_number + 1

            # Displays user guesss on top of semi-redacted secret word
            letters_in_word, letters_in_guess = list_of_letters(word), list_of_letters(guess)
            list_of_guesses.append(f"{guess.upper()} - Your {p.number_to_words(p.ordinal(guess_number))} guess\n{generate_answer_word(letters_in_guess, letters_in_word)} - The magic word")
            print("\n")
            for guess in list_of_guesses:
                print(guess)

            # Lets user know if any of the letters in their guess are in the secret word
            word_set, guess_set = set(letters_in_word), set(letters_in_guess)
            matches = guess_set.intersection(word_set)
            non_matches = guess_set.difference(word_set)
            set_of_new_non_matches = non_matches.difference(set(list_of_letters_not_in_word))
            list_of_letters_not_in_word = sorted(list(set(list_of_letters_not_in_word).union(set_of_new_non_matches)))
            if matches:
                set_of_new_matches = matches.difference(set(list_of_letters_in_word))
                list_of_letters_in_word = sorted(list(set(list_of_letters_in_word).union(set_of_new_matches)))
                print(f"\n\nNot quite\nThe word does contain {p.join(list_of_letters_in_word)}\nThe word does not contain {p.join(list_of_letters_not_in_word, conj='or')}\n")
            elif list_of_letters_in_word and list_of_letters_not_in_word:
                print(f"\n\nNot quite\nThe word does contain {p.join(list_of_letters_in_word)}\nThe word does not contain {p.join(list_of_letters_not_in_word, conj='or')}\n")
            else:
                print(f"\n\nNope, {p.join(list_of_letters_not_in_word)} are not in the magic word\n")
    else:
        print("\n\n\n**********     You Lose     **********\n\n\nThe magic word was ", end="")
        return True


# Checks that the guess is the same length as the word and is in the dictionary we use for the game
def guess_is_valid(user_input, word_length, upper_words):
    while True:
            try:
                guess = user_input.upper()
                if guess in upper_words:
                    return guess
                elif len(guess) != word_length:
                    print(f"\nYour guess must be {p.number_to_words(word_length)} letters long")
                    raise
                else:
                    print("\nSorry, your guess is not in our dictionary")
                    raise
            except:
                user_input = input("\nGuess the magic word: ")


# Converts a word into a list of letters
def list_of_letters(word):
    list_of_letters = []
    list_of_letters[:] = word
    return list_of_letters


# Generates a semi-redacted verson of the secret word by revealing letters if they were guessed in the correct location
# and replacing the letters with "*" otherwise
def generate_answer_word(letters_in_guess, letters_in_word):
    answer_list = []
    for idx, letter in enumerate(letters_in_guess):
        if letter in letters_in_word[idx]:
            answer_list.append(letter)
        else:
            answer_list.append("*")
    return "".join(answer_list)



# Main check
if __name__ == "__main__":
    main()