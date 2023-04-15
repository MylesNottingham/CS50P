# Frank, Ian and Glen’s Letters



# Imports libraries for program
import sys
from pyfiglet import Figlet
figlet = Figlet()

# Checks that the command-line input is in the correct format and prompts user with helpful error messages if not.
# If input is correct this determines if the user wants a random or selected font.
def main():
    if bool(sys.argv[1:3]):
        if sys.argv[1] in ["-f", "--font"]:
            if sys.argv[2] in figlet.getFonts():
                selected_font(input("Input: "))
            else:
                sys.exit("Second argument is not a valid font")
        else:
            sys.exit('First argument must be "-f" or "--font"')
    else:
        random_font(input("Input: "))

# Uses command-line input to set input font and outputs formatted text
def selected_font(input):
    figlet.setFont(font=sys.argv[2])
    print("Output:\n" + figlet.renderText(input))

# Randomly sets input font and outputs formatted text
def random_font(input):
    from random import choice
    figlet.setFont(font=choice(figlet.getFonts()))
    print("Output:\n" + figlet.renderText(input))

main()