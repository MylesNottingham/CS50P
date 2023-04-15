# Fuel Gauge



# Prompts user for amount as a fraction and converts it to a conditional percentage
# If error occurs program will prompt user for input again
def main():
    while True:
        try:
            conditional_percentage = convert_fraction(input("Fraction: "))
            print(conditional_percentage)
            break
        except:
            pass

# Splits fraction into list of values, assigns variables to those values, divides those variables, and converts quotient to rounded integer for percentage
# Returns percentage value if 2-98 %, returns "F" if 99-100 %, and returns "E" if 0-1 %
# Raises error if value falls outside of those conditions
def convert_fraction(fraction):
    fraction_values = fraction.split("/")
    X = int(fraction_values[0])
    Y = int(fraction_values[1])
    level = X / Y
    percentage = round(level * 100)
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        raise

main()