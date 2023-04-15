# Refueling



# Prompts user for amount as a fraction and converts it to a conditional percentage
# If error occurs program will prompt user for input again
def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
            conditional_percentage = gauge(percentage)
            print(conditional_percentage)
            break
        except:
            pass

# Splits fraction into list of values, assigns variables to those values, divides those variables, and converts quotient to rounded integer for percentage.
def convert(fraction):
    fraction_values = fraction.split("/")
    X = int(fraction_values[0])
    Y = int(fraction_values[1])
    level = X / Y
    percentage = round(level * 100)
    return percentage

# Returns percentage value if 2-98 %, returns "F" if 99-100 %, and returns "E" if 0-1 %
# Raises error if value falls outside of those conditions
def gauge(percent):
    if 1 < percent < 99:
        return f"{percent}%"
    elif 99 <= percent <= 100:
        return "F"
    elif 0 <= percent <= 1:
        return "E"
    else:
        raise

# Main check
if __name__ == "__main__":
    main()