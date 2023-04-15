# Watch on YouTube



# Imports library for program
import re

# Takes HTML as prompted user input and prints "youtu.be" equivalent if it is present.
def main():
    print(parse(input("HTML: ")))

# Ensures input has youtube address as "src", extracts video ID from that input,
# and returns video ID formatted as a shareable link.
def parse(s):
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s, re.IGNORECASE):
        return("https://youtu.be/" + matches.group(1))

# Main check
if __name__ == "__main__":
    main()