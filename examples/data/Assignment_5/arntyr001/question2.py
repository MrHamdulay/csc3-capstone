"""Program to simulate vending machine dispensing change
ARNTYR001
17 April 2014"""


amt_paid=0
cost = eval(input("Enter the cost (in cents):\n"))

while cost>amt_paid:
    amt_paid += eval(input("Deposit a coin or note (in cents):\n"))

change_in_cents = amt_paid - cost

if_change=change_in_cents

change_in_dollars = change_in_cents//100

change_in_cents = change_in_cents - 100*change_in_dollars

change_in_quarters = change_in_cents//25

change_in_cents = change_in_cents - 25*change_in_quarters

change_in_10 = change_in_cents//10

change_in_cents = change_in_cents - 10*change_in_10

change_in_5 = change_in_cents//5

change_in_cents = change_in_cents - 5*change_in_5

change_in_1 = change_in_cents


if if_change:
    
    print("Your change is:")
    
    if change_in_dollars>0:
        print(change_in_dollars, "x $1")
    
    if change_in_quarters>0:
        print(change_in_quarters, "x 25c")
    
    if change_in_10>0:
        print(change_in_10, "x 10c")
    
    if change_in_5>0:
        print(change_in_5, "x5c")
    
    if change_in_1>0:
        print(change_in_1, "x5c" )


