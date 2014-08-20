"""Dzunisani Nyoni
2014-04-16
A program that works like a vending machine"""

amount=0
cost=eval(input("Enter the cost (in cents):\n"))
end=''
while amount<cost:
    amount+=eval(input("Deposit a coin or note (in cents):\n"))
    

if amount>cost:
    change=amount-cost
    
    if len(str(change))>=1:
        print("Your change is:")
        
        dollar=change//100
        
        change=change-(100*dollar)
        if dollar>0:
            
            print(dollar, "x $1")
        
        if change==0:
            end=1
            
        
        twentyfive=change//25
        
        change=change-(25*twentyfive)
        
        if twentyfive>0 and end!=1:
            print(twentyfive, "x 25c")
        if change==0:
            end=1
        
        ten=change//10
        change=change-(10*ten)
        
        if ten>0 and end!=1:
            print(ten, "x 10c")
        
        if change==0:
            end=1
        
        five=change//5
        
        change=change-(5*five)
        if five>0 and end!=1:
            print(five, "x 5c")
        if change==0:
            end=1  
        
        
        one=change
        if one>0 and end!=1:
            print(one, "x 1c")
          
        
        #if dollar>0:
        
    #print("Your change is:")
    #print(dollar,"x $1")
    #print(x, "x 25c")
    
    #print(change)
    
    
    