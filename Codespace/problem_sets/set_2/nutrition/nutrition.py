# Nutrition Facts



# Prompts user for input and formats it into title case to match dictionary keys
item = input("Item: ").title()

# Dictionary associating fruit with calories
nutrition_dict = {
    "Apple" : 130,
    "Avocado" : 50,
    "Banana" : 110,
    "Cantaloupe" : 50,
    "Grapefruit" : 60,
    "Grapes" : 90,
    "Honeydew Melon" : 50,
    "Kiwifruit" : 90,
    "Lemon" : 15,
    "Lime" : 20,
    "Nectarine" : 60,
    "Orange" : 80,
    "Peach" : 60,
    "Pear" : 100,
    "Pineapple" : 50,
    "Plums" : 70,
    "Strawberries" : 50,
    "Sweet Cherries" : 100,
    "Tangerine" : 50,
    "Watermelon" : 80
}

# Prints the calories(formatted into a string) in the fruit inputted as long as it is in the top 20 list
if item in nutrition_dict:
    print("Calories: " + str(nutrition_dict[item]))
