""" sigh sigh sigh.... lol.... have to remind mysel to think through
Fionna M"""

deposit = 0
remainder = 0
cost = eval(input("Enter the cost (in cents):\n"))
if cost != 0:
    while True:
        deposit += eval(input("Deposit a coin or note (in cents):\n"))
        if deposit >= cost:
            break
    change = deposit - cost
    
    #check which coins the change is made up of
    
    if change != 0:
        print("Your change is:")  
    if change >= 100:
        remainder = change//100
        print(remainder,"x $1")
        change = change - remainder*100
    if change >= 25:
        remainder = change//25
        print(remainder,"x 25c")
        change = change - remainder*25
    if change >= 10:
        remainder = change//10
        print(remainder, "x 10c")
        change = change - remainder*10
    if change >= 5:
        remainder = change//5
        print(remainder, "x 5c")
        change = change - remainder*5
    if change >= 1:
        print(change, "x 1c")
    
    
