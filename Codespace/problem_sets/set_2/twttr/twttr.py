# Just setting up my twttr



# Prompts user for input
text = input("Input: ")

# Creates a mapping table for the .translate string method to use
vowels = "aeiouAEIOU"
txt = text.maketrans("", "", vowels)

# Prints the stripped down text
print("Output:", text.translate(txt))