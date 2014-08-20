# question2.py
# camilla craven
# vending machine program which calculates your change based on how much you've paid
# 13 April 2014

cost = eval(input("Enter the cost (in cents):\n")) # prompts user to enter item cost

if cost > 0: # setting restriction (has to be cost price)
    
    total = 0 # setting starting amount of money at 0 (no money paid)
    
    while total<cost: # loop for when total amount paid does not exceed cost of item
        add = eval(input("Deposit a coin or note (in cents):\n")) # prompts user for amount paid (in cents)
        total = total + add # adds amount entered to the previous amounts entered (to the total)
    
    change = total - cost # calculates the amount of change needed by subtracting cost of item from total paid
    dollar = change//100 # calculates amount of change that is in dollars
    quarter = (change%100)//25 # calculates amount of change that is in quarters
    ten_cents = ((change%100)%25//10) # calculates amount of change that is in 10 cents
    five_cents = (((change%100)%25)%10)//5 # calculates amount of change that is in 5 cents
    one_cent = ((((change%100)%25)%10)%5)//1 # calculates the amount of change that is in 1 cents
    
    if change > 0: # setting restriction (only if there is change)
        print("Your change is:")
        if dollar > 0: # if there are any dollars
            print(dollar, "x $1") # prints number of dollars
        if quarter > 0: # if there are quarters
            print(quarter, "x 25c") # prints number of quarters
        if ten_cents > 0: # if there are any ten cent coins
            print(ten_cents, "x 10c") # prints number of ten cent coins
        if five_cents > 0: # if there are any five cent coins
            print(five_cents, "x 5c") # prints number of five cent coins
        if one_cent > 0: # if there are any one cent coins
            print(one_cents, "x 1c") # prints number of one cent coins