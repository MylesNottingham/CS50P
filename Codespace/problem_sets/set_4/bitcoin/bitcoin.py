# Bitcoin Price Index

# Imports libraries for program to function
import requests, sys

# Assigns CLI input to variable "number" as float, requests current bitcoin price info from coindesk API,
# assigns correct nested USD exchange rate value as float to variable, multiplies exchange rate and user input,
# and finally displays value in requested format.
try:
    number = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    jr = response.json()
    rate = jr["bpi"]["USD"]["rate_float"]
    exchange = rate * number
    print(f"${exchange:,.4f}")

# Handles various errors with sys.exit() and appropriate messages.
except requests.RequestException:
    sys.exit()
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")