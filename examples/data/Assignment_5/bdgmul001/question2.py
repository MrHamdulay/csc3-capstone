# Vending machine simulation program
# Badugela Mulisa
# 14 April 2014

def V_mechine():
    cost = eval(input("Enter the cost (in cents):\n")) # user inputs cost
    deposit=0
    total = 0
    
    while deposit<cost:
        deposit=deposit+eval(input("Deposit a coin or note (in cents):\n")) #if the deposit is less than the cost prompt the user to deposit again
               
    if cost < deposit:
        total = (deposit - cost) # finds the difference between money deposited and cost
                
        if total!=0:
            print("Your change is:")
        
        one_dollar = (total//2)//(50)
        if one_dollar!=0:
                print(one_dollar,"x $1")# dispays change in terms of 1$
        
        twentyfive_cents = (total - one_dollar*100)//25
        if twentyfive_cents!=0:
            print(twentyfive_cents, "x 25c")# dispays change in terms of 25c
        ten_cents = (total - one_dollar*100 - twentyfive_cents*25)//10
        if ten_cents !=0:
            print(ten_cents,"x 10c")# dispays change in terms of 10c
            
        five_cents = (total - one_dollar*100 - twentyfive_cents*25 - ten_cents*10)//5
        if five_cents != 0:
            print(five_cents,"x 5c")# dispays change in terms of 5c
            
        one_cent = (total - one_dollar*100 - twentyfive_cents*25 - ten_cents*10 - five_cents*5)//1
        if one_cent !=0:
            print(one_cent,"x 1c")# dispays change in terms of 1c

            
V_mechine()          