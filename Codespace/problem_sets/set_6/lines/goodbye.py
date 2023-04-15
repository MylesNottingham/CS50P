def main():
    name = input("What's your name? ")
    print(goodbye(name))


def goodbye(to="world"):
    return f"goodbye, {to}"


if __name__ == "__main__":
    main()