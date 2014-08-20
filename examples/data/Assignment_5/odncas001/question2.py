"""program for calculating change as a vending machine might
casey o'donnell
15 april 2014"""

cost=eval(input("Enter the cost (in cents):\n"))
dep=0
while dep<cost:
    depmore=eval(input("Deposit a coin or note (in cents):\n"))
    dep=dep+depmore
change=dep-cost
if change!=0:
    print("Your change is:")
while change != 0:
    if change//100:
        print(change//100,"x $1")
        change=change%100
    elif change//25:
        print(change//25,"x 25c")
        change=change%25
    elif change//10:
        print(change//10,"x 10c")
        change=change%10
    elif change//5:
        print(change//5,"x 5c")
        change=change%5
    else:
        print(change,"x 1c")
        change=0
        
