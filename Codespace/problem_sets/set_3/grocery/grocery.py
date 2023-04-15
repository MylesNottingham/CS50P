# Grocery List



# Prompts user for input and converts it to a list in upper case(the comma is there in case the user inputs a multi-word item)
# While loop prompts user for additional items and adds them to the list
try:
    item = input().upper()
    item_list = item.split(",")
    while True:
        new_item = input().upper()
        item_list.append(new_item)

# Once user inputs 'control-d' this will check for a list.
# If a list exists this will sort the list alphabetically then run the list through a counter
# The counter converts the list to a dictionary in which each item a key and a numerical value is assigned to that key based on frequency of item.
# Lasty, this displays the value next to the key line-by-line
except EOFError:
    try:
        sorted_list = sorted(item_list)
        from collections import Counter
        sorted_dict = Counter(sorted_list)
        for dict_item, number in sorted_dict.items():
            print (number, dict_item)
    except:
        pass