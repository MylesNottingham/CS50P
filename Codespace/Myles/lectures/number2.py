while True:
    y = input("What's x? ")
    try:
        x = int(y)
    except ValueError:
        print(f"{y} is not an integer")
    else:
        break

print(f"x is {x}")