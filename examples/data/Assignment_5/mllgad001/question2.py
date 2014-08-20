# program to simulate a vending machine and calculate change based on the amount paid
# Gadija Moollagie
# 17 April 2014

cost = eval(input("Enter the cost (in cents):\n")) # prompts user to enter the cost

if cost > 0: # as long as cost>0, prompts user to deposit something
    dep = eval(input("Deposit a coin or note (in cents):\n"))
    pay = 0
    one_cents = 0
    five_cents = 0
    ten_cents = 0
    twentyFive_cents = 0
    hundreds = 0
    # create variables of all types of money to use them later
    
    while dep < cost: # continue through loop until deposit is more than cost
        pay = eval(input("Deposit a coin or note (in cents):\n")) # prompts user to deposit more 
        dep = dep + pay
    change = dep - cost # calculates leftover change
    
    while change >= 100: # calculates number of dollar change needed
        change = change - 100 # leftover change after subtracting 100c change
        hundreds = hundreds + 1
        
    while 25 <= change < 100: # calculates number of 25c change
        change = change - 25 # leftover change after subtracting 25c change
        twentyFive_cents = twentyFive_cents + 1
        
    while 10 <= change < 25: # calculates number of 10c change needed
        change = change - 10 # leftover change after subtracting 10c change
        ten_cents = ten_cents +1
        
    while 5 <= change < 10:
        change = change - 5
        five_cents = five_cents + 1
        
    while 1 <= change < 5:
        change = change - 1
        one_cents = one_cents + 1
        
    if hundreds > 0 or twentyFive_cents>0 or ten_cents>0 or five_cents>0 or one_cents>0:
        # if there is any type of change leftover
        print("Your change is:")
        
        if hundreds>0: # if there is change of 100c
            print(hundreds, 'x',  '$1')
            
        if twentyFive_cents>0: # if there is change of 25c
            print(twentyFive_cents, 'x', '25c')
            
        if ten_cents>0: # if there is change of 10c
            print(ten_cents, 'x', '10c')
            
        if five_cents>0: # if there is change of 5c
            print(five_cents, 'x', '5c')
            
        if one_cents>0: # if there is change of 1c
            print(one_cents, 'x', '1c')
            