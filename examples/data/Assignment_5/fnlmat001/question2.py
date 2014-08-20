"""Program to simulate a vending machine and calculate change based on the amount paid
Matthew Finlayson - FNLMAT001
15/04/2014"""

cost = eval(input("Enter the cost (in cents):\n"))
amountPaid = 0
while cost>amountPaid:
    paid = eval(input("Deposit a coin or note (in cents):\n"))
    amountPaid+=paid

change = amountPaid-cost


if(change != 0):
    print("Your change is:")
    for i in [100, 25, 10, 5, 1]: # i takes on the coin values of the 1$ through to 1c
        if (change != 0):
            numCoins = change//i # determines how many multiples of the current coin value is needed to make up the change
            change -= numCoins*i # the amount of change needed is decreased according to the number of coins given and the coin value
            if (numCoins != 0): # makes sure the change is only displayed if the coins of that value are needed
                if (i == 100):
                    print(numCoins,"x $1")
                elif (i == 25):
                    print(numCoins,"x 25c")
                elif (i == 10):
                    print(numCoins,"x 10c")
                elif (i == 5):
                    print(numCoins,"x 5c")
                else:
                    print(numCoins,"x 1c")
        
        