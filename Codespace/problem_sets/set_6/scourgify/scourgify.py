# Scourgify


# Imports libraries for program
import sys, csv

# Creates list for student data to be appended to.
students = []

# Takes two csv files as command line input and, if valid,
# uses first file as input to write to second file.
def main():
    command_line_input = sys.argv
    if input_check(command_line_input):
        read_csv(command_line_input[1])
        write_csv(command_line_input[2])
        sys.exit(0)
    else:
        sys.exit(1)

# Verifies command line input is valid by checking:
#   for the correct number of arguments
#   if the file ends in ".csv"
#   if the file exists
# Returns feedback and exits program if it is not valid
def input_check(input):
    if len(input) == 3:
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
    elif len(input) < 3:
        print("Too few command-line arguments")
        return False
    else:
        print("Too many command-line arguments")
        return False

# Creates list of students from existing csv file
def read_csv(CSV1):
    with open(CSV1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = (row["name"])
            last, first = student.split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})

# Creates formatted csv of students from list
def write_csv(CSV2):
    with open(CSV2, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow({
                "first": student["first"],
                "last": student["last"],
                "house": student["house"]
                })

# Main check
if __name__ == "__main__":
    main()