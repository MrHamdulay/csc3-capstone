# Kate Bell
# BLLKAT005
# 16 April 2014 

cost = eval(input("Enter the cost (in cents):\n"))
paid = 0

# Determine how much is paid (must be >= cost)
while paid < cost: 
    paid = paid + eval(input("Deposit a coin or note (in cents):\n"))
    
# Determine how much change is due    
change = paid - cost

# Divide change up into different coin values
if change != 0:
    print("Your change is:")
    dollar_change = change//100 
    if dollar_change != 0: 
        print (dollar_change,"x $1")
        change=change-dollar_change*100
    
    quarter_change = change//25 
    if quarter_change != 0: 
        print (quarter_change,"x 25c")
        change=change-quarter_change*25
    
    dime_change = change//10
    if dime_change != 0: 
        print (dime_change,"x 10c")
        change=change-dime_change*10
        
    nickel_change = change//5 
    if nickel_change != 0: 
        print (nickel_change,"x 5c")
        change=change-nickel_change*5    
    
if change != 0:    
    print (change,"x 1c")
    change=0
        