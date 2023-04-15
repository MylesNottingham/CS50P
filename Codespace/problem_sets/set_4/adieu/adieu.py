# Adieu, Adieu



# Imports library for program
import inflect
p = inflect.engine()

# Creates a blank list, prompts user for name, adds name to end of list, prompts user again
# When user breaks program it prints names in requested format
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except:
        print("\nAdieu, adieu, to " + p.join(name_list))
        break