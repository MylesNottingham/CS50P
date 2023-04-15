# Guessing Game



# Imports library for program
import random
from sys import exit

# Prompts user for upper level to define range, generates random number in that range, initiates game using that number, and exits upon correct guess.
def main():
    defined_range = get_level()
    random_number = generate_number(defined_range)
    exit(play_game(random_number))

# Prompts user for level and adds one to level so that range is inclusive. Re-prompts if level not greater than or equal to one.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1:
                level += 1
                return(level)
            else:
                raise
        except:
            pass

# Generates random integer between 1 and user defined max for range.
def generate_number(max):
    number = random.randrange(1, max)
    return(number)

# Prompts user to guess the number. If user guesses incorrectly this uses additional prompts to guide user to correct answer.
# Once user guesses correctly this sends message to terminates program.
def play_game(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if 0 < guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
            elif guess == n:
                return("Just right!")
            else:
                raise
        except:
            pass

main()