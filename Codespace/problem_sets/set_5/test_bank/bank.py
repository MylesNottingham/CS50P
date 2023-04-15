# Back to the Bank


# Imports libraries for program
import sys
# Prompts user for greeting, asseses value, displays reward
def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

# Lowers case and removes leading whitespace from greeting, checks greeting for leading "hello" or leading "h",
# and returns appropriate reward
def value(greet):
    greeting = greet.lower()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100

# Main check
if __name__ == "__main__":
    main()