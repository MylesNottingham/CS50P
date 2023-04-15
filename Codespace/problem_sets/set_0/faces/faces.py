# Making Faces



# Prompts user for input and prints text with emoticons converted to emoji
def main():
    emoticon = input("Show me your mug ")
    print(convert(emoticon))

# Converts emoticons to emoji
def convert(emoji):
    return (emoji).replace(":)","🙂").replace(":(","🙁")

main()