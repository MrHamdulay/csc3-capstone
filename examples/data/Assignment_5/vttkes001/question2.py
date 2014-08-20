""" Vending machine simulator
Keshin Vittee
16 April 2014"""

cost = eval(input("Enter the cost (in cents):\n"))
paid = 0

while paid < cost:
    paid += eval(input("Deposit a coin or note (in cents):\n"))
    
if paid > cost:
    change = paid - cost
    doll = change//100
    change -= 100*doll
    quart = change//25
    change -= 25*quart
    ten = change//10
    change -= 10*ten
    five = change//5
    change -= 5*five
    ones = change
    change -= change
    print("Your change is:")
    if doll != 0:
        print(doll, "x $1")
    if quart != 0:
        print(quart, "x 25c")
    if ten != 0:
        print(ten, "x 10c")
    if five != 0:
        print(five, "x 5c")
    if ones != 0:
        print(ones, "x 1c")    
        
    

