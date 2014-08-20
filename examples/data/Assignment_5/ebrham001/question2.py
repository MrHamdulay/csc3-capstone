'''SIMULATING A VENDING MACHINE
   HAMZA EBRAHIM
   17/04/14'''

# ASSIGNMENT 5 - QUESTION 2


# Prompt the user to enter cost
cost = eval(input("Enter the cost (in cents):\n"))

# amount paid
paid = 0

# indefinite loop - while the amount paid is still less than cost, keep prompting for money

while paid < cost:
    paid += eval(input("Deposit a coin or note (in cents):\n"))
    
# when paid is more than cost offer change    

    if paid > cost:
        change = paid - cost 
        if change != 0:
            print('Your change is:')


# change conversion calculations 

        dollar = change//100
        if dollar != 0:
            print(dollar, 'x $1')
    
        quart = ( (change) - (dollar*100) ) // 25
        if quart != 0:
            print(quart, 'x 25c')
        
        tc = ( (change) - (dollar*100) - (quart*25) ) // 10
        if tc != 0:
            print(tc, 'x 10c')
        
        fc = ( (change) - (dollar*100) - (quart*25) - (tc*10) ) // 5
        if fc != 0:
            print(fc, 'x 5c')
        
        oc = ( (change) - (dollar*100) - (quart*25) - (tc*10) - (fc*5) ) // 1
        if oc != 0:
            print(oc, 'x 1c')
            
# program ends            