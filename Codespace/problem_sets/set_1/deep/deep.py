# Deep Thought



# Promps user for answer, converts to lower case, convers text to digits, and removes whitespace
Q = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
Q = Q.lower()
Q = Q.replace("forty two", "42").replace("forty-two", "42").strip()

# Validates answer
if Q == "42":
    print("Yes")
else:
    print("No")