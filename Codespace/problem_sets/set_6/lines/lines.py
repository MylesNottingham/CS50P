# Lines of Code



# Imports library for program
import sys

# Creates list for validated lines of code to be appended to.
lines = []

# Takes program as command line input and if valid counts and displays number of lines in program.
def main():
    command_line_input = sys.argv
    if input_check(command_line_input):
        count_lines(command_line_input)
        print(len(lines))
        sys.exit(0)
    else:
        sys.exit(1)

# Verifies command line input is valid by checking:
#   for the correct number of arguments
#   if the file ends in ".py"
#   if the file exists
# Returns feedback and exits program if it is not valid
def input_check(input):
    if len(input) == 2:
        if (input[1]).endswith(".py"):
            try:
                open(input[1])
                return True
            except FileNotFoundError:
                print("File does not exist")
                return False
        else:
            print("Not a Python file")
            return False
    elif len(input) < 2:
        print("Too few command-line arguments")
        return False
    else:
        print("Too many command-line arguments")
        return False

# Counts lines of code in program(excluding comments and whitespace)
def count_lines(program):
    with open(program[1]) as file:
        for line in file:
            if line.lstrip().startswith("#"):
                pass
            elif line.isspace():
                pass
            else:
                lines.append(line)

# Main check
if __name__ == "__main__":
    main()