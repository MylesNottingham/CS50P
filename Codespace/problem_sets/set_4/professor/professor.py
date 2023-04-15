# Little Professor



# Imports "randint" from "random" library for program to use to generate random numbers
from random import randint

# Main function establishes a counter and a score, uses user-defined level to generate an equation,
# takes result of user answer to question based on equation and tracks count and users score.
# This repeats ten times and then the toatl score is displayed.
def main():
    level = get_level()
    count = 0
    score = 0
    while count < 10:
        integers = generate_integer(level)
        result = generate_problem(integers)
        if result == "correct":
            score += 1
            count += 1
        elif result == "incorrect":
            count += 1
    print(score)

# Function that prompts user for level and returns level chosen by user if in correct format.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (level == 1
            or level == 2
            or level == 3):
                return level
            else:
                raise ValueError
        except ValueError:
            pass

# Function that uses level to define a range for variables used in equation.
def generate_integer(lvl):
    if lvl == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif lvl == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)
    return (x, y)

# Function that establishes a counter, uses randomly generated integers to create an equation, and prompts user for input to complete partial equation,
# If the user guesses correctly it will display "Correct!" and return "correct" to main function.
# If the user guesses incorrectly it will allow a total of three guesses before returning "incorrect" to main function.
def generate_problem(n):
    count = 0
    x = n[0]
    y = n[1]
    z = n[0] + n[1]
    while count < 3:
        guess = input(f"{x} + {y} = ")
        try:
            if int(guess) == z:
                return "correct"
            else:
                raise ValueError
        except ValueError:
            print("EEE")
            count += 1
    if count == 3:
        print(f"{x} + {y} = {z}")
        return "incorrect"

# Main check
if __name__ == "__main__":
    main()