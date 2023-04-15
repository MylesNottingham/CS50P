# Purdle
#### Video Demo:  <https://youtu.be/GD_azlvT5D0>
#### Description: Welcome to Purdle!

This is my Wordle inspired command-line game in Python for CS50P.

The program starts by importing a few libraries for the program to use. Namely, "random", "inflect", and from "english_dictionary", "get_dict".
Then these libraries are set up to use by assigning "get_dict" to the "english_dict" variable and "inflect" to the "p" variable.

Next, the "main" function is defined.
It starts out by calling an "intro" function, whose purpose is to greet and succinctly explain the basic rules and operations of the game.

The next line calls the "select_word_length" function that takes user input, prompted by the "how_many_letters" function, as an argument and assigns its return value to the variable "word_length".
The "select_word_length" function is a loop that prompts the user to input an integer between one and ten, error checks, and returns the value.
The next line calls the "select_number_of_guesses" function that takes user input, prompted by the "how_many_guesses" function, as an argument and assigns its return value to the variable "number_of_guesses".
The "select_number_of_guesses" function is a loop that prompts the user to input an integer between five and twenty-five, error checks, and returns the value.

The next line in "main" calls the "randomly_generate_word" function using the "word_length" variable as an argument and assigns its return value to the "word" and "upper_words" variables, respectively.
The "generate_words" function first converts the "english_dict" dictionary to a list of just "english_words". Then it filters that list down to words with the number of letters specified in "word_length" and creates a new list assigned to the "words" variable. Then a blank list is created as the "upper_words" variable. Next, a for loop is started that converts the "word" list to uppercase under the "upper_words" variable. Finally, it calls on the "random" library to pick a random word and then returns that value and the "upper_words" list.

The next line calls the "guessing_game" function as a conditional to an if statement and passes in the "word", "word_length", "upper_words", and "number_of_guesses" variables as arguments.
The "guessing_game" function starts by converting the random word to all-caps. Then a variable called "guess_number" is assigned an int value of 0. Then, blank lists are created and assigned to the "list_of_guesses", "list_of_letters_in_word", and "list_of_letters_not_in_word" variables. Finally, a message is displayed letting the user know the word has been chosen and the game has begun.

After that a while loop is started based on the "number_of_guesses" the user previously selected.
The loop will run until you either win or run out of guesses.
For each iteration of the loop the user will be reminded of their "number_of_guesses" remaining. Then the "guess_is_valid" function will prompt the user to "guess" the secret word. It also takes in the "word_length" and "upper_words" variables as arguments.

The "guess_is_valid" function is a while loop that checks that the guess is a real possibility. It first uppercases "guess" and checks to see that it is in the dictionary we use for the game. If so it will return the value of "guess". If the "guess" does not have the same number of characters as "word_length" an error will be raised and the user will be informed why and re-prompted. If the "guess" is not in our dictionary an error will be raised and the user will be informed why and re-prompted.

The "guess" will then be compared to the "word" and if the "guess" matches the "word" the user will be informed and the function will return "True".
If the "guess" does not match the "word", an else statement begins.
Then a guess is subtracted from the "number_of_guesses" and added to the "guess_number" variables respectively.

Now the function "list_of_letters" is called on both "word" and "guess" and the return values are assigned to "letters_in_word" and "letters_in_guess" respectively.
The "list_of_letters" function takes in each word as an argument and splits that word into a list of individual letters.

The next line appends your guess with a label, calls the "generate_answer_word" function, and appends its return value with a label underneath the guess in the "list_of_guesses".
The "generate_answer_word" function compares the "letters_in_guess" to the "letters_in_word". For every matching letter it will append that letter to the "answer_list". For every non-matching letter it will append a "*" to the list. The "answer_list" is then joined and returned.

Line break for readability

The next line is a for loop that displays each element individually in the "list_of_guesses"

The next line converts the lists of letters for the guess and word and converts them to sets.
Then the sets are compared and if any letters match, regardless of location, it will assign them to a variable called "matches".
Any letters that are in your guess that are not in the word are added to "non_matches"
If any guess letters did not match letters in the word and were not previously guessed, they will be assigned to "set_of_new_matches". Then that set will be joined to "set(list_of_letters_not_in_word)". This combination set will be converted to a list, sorted alphabetically, and assigned to overwrite the "list_of_letters_not_in_word" variable.

Now a conditional begins.
If any letters matched the word that were not previously guessed, they will be assigned to "set_of_new_matches". Then that set will be joined to "set(list_of_letters_in_word)". This combination set will be converted to a list, sorted alphabetically, and assigned to overwrite the "list_of_letters_in_word" variable.
Finally, by use of an "else if", all letters that have been correctly guessed throughout the game regardless of the current turn will be displayed to the user.
If none of the letters matched it will let the user know that as well.

The very last two lines are what actually calls main and gets this all going.