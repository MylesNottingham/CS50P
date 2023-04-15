# Seasons of Love



# Imports libraries for program
from datetime import date
import inflect, sys
p = inflect.engine()


# Takes birthday as iso-formatted input and prints age in minutes
def main():
    birthday = get_birthday(input("Date of Birth: "))
    age = get_age(birthday)
    time_written_as_minutes = format_time(age)
    print(time_written_as_minutes)

# Converts user input to date-classed data or exits program if formatting is incorrect
def get_birthday(input):
    try:
        return date.fromisoformat(input)
    except:
        sys.exit("Invalid date")

# Subtracts birthday from today's date
def get_age(birthday):
    return (date.today() - birthday)

# Converts timedelta to minutes as words
def format_time(age):
    minutes = (age.days * 1440)
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


# Main check
if __name__ == "__main__":
    main()