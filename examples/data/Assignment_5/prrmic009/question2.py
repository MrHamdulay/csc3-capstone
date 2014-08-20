""" program to calculate change in coins produced by vending machine 
for input priced item and input values of payment
Mick Perring
16 April 2014"""

def vending_change ():
    cost = eval(input("Enter the cost (in cents):\n")) # lets user input cost (in cents)
    cash = 0
    while cash < cost:
        cash += eval(input("Deposit a coin or note (in cents):\n")) # lets user input money values until
    change = cash - cost # calculates change                        # value equals or exceeds cost
    if change != 0:
        # prints change values in coins - 1$, 25c, 10c, 5c and 1c
        print ("Your change is:")
        n = change//100
        if n != 0:
            print (n,"x $1")
        change -= n*100
        n = change//25
        if n != 0:
            print (n,"x 25c")
        change -= n*25
        n = change//10
        if n != 0:
            print (n,"x 10c")
        change -= n*10
        n = change//5
        if n != 0:
            print (n,"x 5c")
        change -= n*5
        n = change
        if n != 0:
            print (n,"x 1c")
        
vending_change ()
    