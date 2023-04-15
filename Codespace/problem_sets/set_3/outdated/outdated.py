# Outdated



# Prompts user for date and converts it to ISO format
# If error occurs program will prompt user for input again
def main():
    while True:
        try:
            ISO_date = convert_date(input("Date: "))
            print(ISO_date)
            break
        except:
            pass

# Determines date format and splits date into list of values then checks that the values are logical and assigns variables to those values
# Returns date data formatted and rearranged
# Raises error if value falls outside of those conditions
def convert_date(date):
    if "/" in date:
        date_values = date.split("/")
        month = int(date_values[0])
    elif "," in date:
        date_values = date.replace(",", "")
        date_values = date_values.split()
        month = date_values[0]
        month = month_dict[month]
    else:
        raise

    if month > 12:
        raise
    day = int(date_values[1])
    if day > 31:
        raise
    year = int(date_values[2])

    return f"{year:04}-{month:02}-{day:02}"

# Dictionary to link text month with integer
month_dict = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12,
}

main()