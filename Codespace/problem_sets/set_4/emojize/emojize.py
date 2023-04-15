# Emojize



# Imports the "emoji" library from package that was previously installed
import emoji

# Takes in input, runs it through the "emojize" function in the "emoji" library, prints the output.
text = input("Input: ")
emo = emoji.emojize(text, language="alias")
print("Output: " + emo)