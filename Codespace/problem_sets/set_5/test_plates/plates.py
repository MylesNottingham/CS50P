# Re-requesting a Vanity Plate



# Checks to see if input is valid
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Runs input through a series of checks
def is_valid(s):
    if (is_between_two_and_six(s)
    and first_two_alpha(s)
    and alphanumeric_only(s)
    and number_check(s)
    ):
        return True
    else:
        return False


# Checks that input is between two and six charachters
def is_between_two_and_six(p):
    if 2 <= len(p) <= 6:
        return True

# Checks that first two charachters of input are letters
def first_two_alpha(p):
    p = p[0:2]
    if p.isalpha():
        return True

# Checks that input is alphanumeric only
def alphanumeric_only(p):
    if p.isalnum():
        return True

# Checks if input has any digits and if it does:
# It removes leading alpha then checks that it ends with only digits and the digits do not begin with zero
def number_check(p):
    import string
    letters = string.ascii_letters
    stripped_alpha_dict = p.maketrans("", "", letters)
    stripped_alpha = p.translate(stripped_alpha_dict)
    has_digits = stripped_alpha.isdigit()

    if has_digits:
        leading_alpha_removed = p.lstrip(letters)

        end_is_digit = leading_alpha_removed.isdigit()
        first_not_0 = int(leading_alpha_removed[0]) != 0

        if end_is_digit and first_not_0:
            return True
        else:
            return False
    else:
        return True

# Main check
if __name__ == "__main__":
    main()