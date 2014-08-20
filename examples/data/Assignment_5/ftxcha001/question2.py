#Chantel Foot
#Assignment 5, question 2


cost = eval(input("Enter the cost (in cents):\n"))

if cost == 0 or cost <0:
    print() #do not ask for money to be deposited if no cost present
    
if cost>0: 
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    while deposit < cost: #more money needs to be put in, so keep asking until full cost amount has been inserted.
        
        additional_amount = eval(input("Deposit a coin or note (in cents):\n"))
        deposit= deposit + additional_amount
        
    if cost == deposit:
        print("") #this means that exact amount has been put in. no change needs to be given out
        
    else: #change needs to be given 
        
        change = deposit - cost #new deposit amount = deposit + additional amounts
        dollars = change//100 #how much of each coin, "//" yields natural number
        twentyfive_cents = (change-(dollars*100))//25 # *100 to get back to cents i.e 2x100=200
        ten_cents = (change-(dollars*100)- (twentyfive_cents*25))//10 
        five_cents = (change-(dollars*100)- (twentyfive_cents*25)- (ten_cents*10))//5
        one_cents = (change-(dollars*100)- (twentyfive_cents*25)- (ten_cents*10)- (five_cents*5))//1
        
        print("Your change is:")
        if dollars != 0: 
            print(dollars,"x $1")
        if twentyfive_cents != 0:
            print(twentyfive_cents,"x 25c")
        if ten_cents != 0:
            print(ten_cents,"x 10c")
        if five_cents !=0:
            print(five_cents,"x 5c")
        if one_cents !=0:
            print(one_cents,"x 1c")
            
            
            
            
        
                            
        
        
        
        
        
        
        
        
        
        
            
            
            