# Meal Time



# Takes in time as a raw input in 12hr or 24hr format, converts it to decimal form,
# determines if it is time for a meal and if so which one, and prints the result
def main():
    raw_time = input("What time is it? ")
    decimal = convert(raw_time)
    if 7 <= decimal <= 8:
        print("breakfast time")
    elif 12 <= decimal <= 13:
        print("lunch time")
    elif 18 <= decimal <= 19:
        print("dinner time")


# Converts raw time to a decimal form
def convert(time):
    # Cleans up the user input
    time = time.lower().replace(" ","").replace(".","")
    # Converts hour portion to 24hr form and splits minute off
    if time.endswith("pm") == True:
        time = time.removesuffix("pm")
        hour, minute = time.split(":")
        hour = int(hour)
        if hour == 12:
            hour = 0
        hour = hour + 12
    elif time.endswith("am") == True:
        time = time.removesuffix("am")
        hour, minute = time.split(":")
        hour = int(hour)
        if hour == 12:
            hour = 0
    else:
        hour, minute = time.split(":")
        hour = int(hour)

    # Converts minute portion to decimal form
    minute = int(minute) / 60

    # Adds converted hours and minutes and returns time as 24hr decimal
    decimal = hour + minute
    return decimal

# This portion of the code was supplied as-is
if __name__ == "__main__":
    main()