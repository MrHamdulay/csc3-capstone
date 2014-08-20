#Nicholas Mazower, MZWNIC001
#18/04/2014
#Change output calculator (in USD coins)


cost=eval(input("Enter the cost (in cents):\n"))

deposit = 0

def pay():
    global deposit
    deposit=deposit+eval(input("Deposit a coin or note (in cents):\n"))
#Coin names are their tradtional American ones
if cost>0:
    pay()
    change=0
    dollars=0
    quarters=0
    nickels=0
    dimes=0
    pennies=0
    while cost>deposit:
        pay()
    
    
    
    change=deposit-cost
    dollars=change//100
    change=change-100*dollars
    quarters=change//25
    change=change-25*quarters
    dimes=change//10
    change=change-10*dimes
    nickels=change//5
    change=change-5*nickels
    pennies=change
    if (deposit-cost)>0:
        print("Your change is:")
    if dollars>0:
        print(dollars, "x $1")
    if quarters>0:
        print(quarters, "x 25c")
    if dimes>0:
        print(dimes, "x 10c")
    if nickels>0:
        print(nickels, "x 5c")
    if pennies>0:
        print(pennies, "x 1c")
