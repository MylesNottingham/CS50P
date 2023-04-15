# Pizza Py



# Imports libraries for program
import sys, csv
from tabulate import tabulate

# Creates list for validated menu items to be appended to.
menu = []

# Takes csv file as command line input and if valid displays as table.
def main():
    command_line_input = sys.argv
    if input_check(command_line_input):
        make_table(command_line_input[1])
        print(tabulate(menu, headers="firstrow", tablefmt="grid"))
        sys.exit(0)
    else:
        sys.exit(1)

# Verifies command line input is valid by checking:
#   for the correct number of arguments
#   if the file ends in ".csv"
#   if the file exists
# Returns feedback and exits program if it is not valid
def input_check(input):
    if len(input) == 2:
        if (input[1]).endswith(".csv"):
            try:
                open(input[1])
                return True
            except FileNotFoundError:
                print("File does not exist")
                return False
        else:
            print("Not a CSV file")
            return False
    elif len(input) < 2:
        print("Too few command-line arguments")
        return False
    else:
        print("Too many command-line arguments")
        return False

# Converts csv file to list to be used to make table
def make_table(CSV):
    with open(CSV) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append({"column_0": row[0], "column_1": row[1], "column_2": row[2]})

# Main check
if __name__ == "__main__":
    main()