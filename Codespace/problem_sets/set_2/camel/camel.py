# camelCase



# Prompts user for input in Camel Case, converts it to Snake Case, removes leading "_", and prints result
def main():
    camel = input("camelCase: ")
    snake = camel.translate(letters).lstrip("_")
    print("snake_case: " + snake)

# Dictionary for the .translate string method
letters = {
    65 : "_a",
    66 : "_b",
    67 : "_c",
    68 : "_d",
    69 : "_e",
    70 : "_f",
    71 : "_g",
    72 : "_h",
    73 : "_i",
    74 : "_j",
    75 : "_k",
    76 : "_l",
    77 : "_m",
    78 : "_n",
    79 : "_o",
    80 : "_p",
    81 : "_q",
    82 : "_r",
    83 : "_s",
    84 : "_t",
    85 : "_u",
    86 : "_v",
    87 : "_w",
    88 : "_x",
    89 : "_y",
    90 : "_z",
}

main()