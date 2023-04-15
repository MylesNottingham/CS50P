# Home Federal Savings Bank



# Prompts user for input then lowers case and removes leading whitespace
g = input("Greeting:").lower().lstrip()

# Checks greeting for leading "hello" or leading "h" and prints appropriate reward
if g.startswith("hello") == True:
    print("$0")
elif g.startswith("h") == True:
    print("$20")
else:
    print("$100")