# CS50 P-Shirt



# Imports libraries for program
import sys, os
from PIL import Image, ImageOps

# Takes two image files as command line input and, if valid,
# uses first image as input, overlays shirt image, and creates second image.
def main():
    command_line_input = sys.argv
    if input_check(command_line_input):
        process_image(command_line_input[1])
        sys.exit(0)
    else:
        sys.exit(1)

# Verifies command line input is valid by checking:
#   for the correct number of arguments
#   if the file ends in ".jpg", ".jpeg", or ".png"
#   if the extensions match
#   if the file exists
# Returns feedback and exits program if it is not valid
def input_check(input):
    if len(input) == 3:
        input[1] = input[1].lower()
        extensions = (".jpg", ".jpeg", ".png")
        if input[1].endswith(extensions):
            if input[2].endswith(extensions):
                extension_1 = os.path.splitext(input[1])
                extension_2 = os.path.splitext(input[2])
                if extension_1[1] == extension_2[1]:
                    try:
                        open(input[1])
                        return True
                    except FileNotFoundError:
                        print("Input does not exist")
                        return False
                else:
                    print("Input and output have different extensions")
                    return False
            else:
                print("Invalid output")
                return False
        else:
            print("Invalid input")
            return False
    elif len(input) < 3:
        print("Too few command-line arguments")
        return False
    else:
        print("Too many command-line arguments")
        return False

# Process image opens "shirt.png" as shirt, resizes input image to match,
# pastes shirt onto input image, and saves as third command line argument.
def process_image(input_image):
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(input_image) as image:
        image = ImageOps.fit(image, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        Image.Image.paste(image, shirt, box=None, mask=shirt)
        Image.Image.save(image, sys.argv[2])

# Main check
if __name__ == "__main__":
    main()