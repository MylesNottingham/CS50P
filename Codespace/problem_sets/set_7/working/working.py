# Working 9 to 5



# Imports library for program
import re

# Takes hour set in 12hr format as prompted user input and displays 24hr format equivalent.
def main():
    print(convert(input("Hours: ")))

# Ensures input in in the correct format(n xM to n xM),
# extracts time as numeric data from that input,
# converts time from 12hr format to 24hr format,
# returns converted time to main() if valid,
# and raises ValueError if invalid.
def convert(s):
    if matches := re.search(r"^([1-9]|1[0-2]):?([0-5][\d])? ([A|P]M) to ([1-9]|1[0-2]):?([0-5][\d])? ([A|P]M)$", s):

# First hour conversion
        hours_1 = int(matches.group(1))
        if matches.group(3) == "AM":
            if hours_1 == 12:
                hours_1 = 0
        else:
            if hours_1 ==12:
                hours_1 = 0
            hours_1 += 12
        if hours_1 < 10:
            hours_1 = f"0{hours_1}"
        else:
            hours_1 = str(hours_1)

# First minute converson
        minutes_1 = matches.group(2)
        if minutes_1 == None:
            minutes_1 = "00"

# Second hour conversion
        hours_2 = int(matches.group(4))
        if matches.group(6) == "AM":
            if hours_2 == 12:
                hours_2 = 0
        else:
            if hours_2 ==12:
                hours_2 = 0
            hours_2 += 12
        if hours_2 < 10:
            hours_2 = f"0{hours_2}"
        else:
            hours_2 = str(hours_2)

# Second minute conversion
        minutes_2 = matches.group(5)
        if minutes_2 == None:
            minutes_2 = "00"

# Formats data and returns to main() or raises error
        return(hours_1 + ":" + minutes_1 + " to " + hours_2 + ":" + minutes_2)
    else:
        raise ValueError


# Main check
if __name__ == "__main__":
    main()