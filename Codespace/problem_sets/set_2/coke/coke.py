# Coke Machine



# Sets the base balance to 50
bal = 50

# While loop that takes input as long as there is a balance but limits input to 5, 10, or 25 "cent coins"
while bal > 0:
    print("Amount Due:", bal)
    coin = input("Insert Coin: ")
    if coin == "5" or coin == "10" or coin == "25":
        coin = coin
    else:
        coin = 0
    bal = int(bal) - int(coin)

# once balance is paid, prints change due, if any
if bal <= 0:
    print("Change Owed:", -bal)