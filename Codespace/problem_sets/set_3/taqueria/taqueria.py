# Felipe’s Taqueria



# Initially defines total as 0 and then starts a loop that prompts user for input, formats it into title case to match dictionary keys, and calls get_cost function on input
# Each loop adds item cost to current total then new total is formatted to 2 decimal places and displayed
# Loop continues until user inputs EOF
def main():
    total = 0
    while True:
        try:
            item_cost = get_cost(input("Item: ").title())
            total = float(total) + item_cost
            total = "{:.2f}".format(total)
            print("Total: $" + str(total))
        except RuntimeError:
            pass
        except EOFError:
            break

# Returns the cost of the item inputted as long as it is on the menu or raises error if input is not on menu
def get_cost(item):
    if item in menu_dict:
        return menu_dict[item]
    else:
        raise

# Dictionary associating menu item with cost in dollars
menu_dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()