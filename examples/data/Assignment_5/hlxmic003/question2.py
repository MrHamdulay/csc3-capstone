# Michaela Heale
# Assignment 5 Question 1
# Vending machine


tote = 0
cost = eval(input("Enter the cost (in cents):\n"))
while True:
    if tote<cost:
        newt = eval(input("Deposit a coin or note (in cents):\n"))
        tote += newt
    elif tote == cost:
        break
    elif tote>cost:
        end = tote - cost
    
        dollar = end//100
        quarter  = (end-100*dollar)//25
        dime = (end-100*dollar-25*quarter)//10
        nickel = (end-100*dollar-25*quarter-10*dime)//5
        penny = (end-100*dollar-25*quarter-10*dime-5*nickel)
    
        print("Your change is:")
        
        if dollar>0:
            print(dollar,"x $1")
        if quarter>0:
            print(quarter,"x 25c")
        if dime>0:
            print(dime,"x 10c")
        if nickel>0:
            print(nickel,"x 5c")
        if penny>0:
            print(penny,"x 1c")
        break

