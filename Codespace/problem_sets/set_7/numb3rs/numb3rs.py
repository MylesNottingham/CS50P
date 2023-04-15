# NUMB3RS



# Imports library for program
import re

# Takes IPv4 address as prompted user input and checks if it is valid
def main():
    print(validate(input("IPv4 Address: ")))

# Ensures input is four numbers between 0-255 separated by periods
def validate(ip):
    ip = ip.strip()
    if re.search(r"^(\d{1,2}\.|1\d{1,2}\.|2[0-4]\d\.|25[0-5]\.){3}(\d{1,2}|1\d{1,2}|2[0-4]\d|25[0-5])$", ip):
        return(True)
    else:
        return(False)

# Main check
if __name__ == "__main__":
    main()