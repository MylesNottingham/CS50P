# Regular, um, Expressions



# Imports library for program
import re

# Takes text as user input and displays number of standalone "um"s contained in it.
def main():
    print(count(input("Text: ")))

# Formats input to make searching easier,
# searches input for standalone "um"s
# returns number of "um"s in list created by re.findall
def count(s):
    s = " " + s.lower().replace(" ", "  ") + " "
    um_list = re.findall(r"[^a-z]um[^a-z]", s)
    return len(um_list)

# Main check
if __name__ == "__main__":
    main()