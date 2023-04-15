# Response Validation



# Imports library for program
from validator_collection import checkers

# Takes email address as prompted user input and displays result
#   of validate function
def main():
    print(validate(input("What's your email address? ")))

# Cleans up input and tests it using the "checkers.is_email"
#   function of "validator_collection".
# If result is True returns "Valid".
# If result is False returns "Invalid".
def validate(email):
    email = email.strip()
    email_check = checkers.is_email(email)
    if email_check == True:
        return "Valid"
    else:
        return "Invalid"

# Main check
if __name__ == "__main__":
    main()