# Testing my twttr



# Main function takes input, removes vowels, prints vowel-less output.
def main():
    twt = shorten(input("Input: "))
    print("Output:", twt)

# Function establishes a translation table of vowels and uses it to remove vowels from input, returning vowel-less output
def shorten(word):
    vowels = "aeiouAEIOU"
    wrd = word.maketrans("", "", vowels)
    return word.translate(wrd)

# Go button
if __name__ == "__main__":
    main()