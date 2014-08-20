"""Vending machine simulator
Ryan Kopping"""

cost = eval(input("Enter the cost (in cents):\n"))
if(cost!=0):
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    remain = cost - deposit
    while (remain>0):
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        remain = (remain-deposit)
        
    
    if(remain!=0):
        print ("Your change is:")    
    
    dollars =0
    cents25=0
    cents10=0
    cents5=0
    cents1=0
    
    while (remain<0):
        if (remain + 100)<=0:
            
            dollars += 1
            remain +=100
            
        elif (remain + 25)<=0:
            
            cents25 += 1
            remain +=25
            
        elif (remain + 10)<=0:
           
            cents10 +=1
            remain +=10
            
        elif (remain + 5)<=0:
           
            cents5 += 1
            remain +=5
        
        elif (remain +1)<=0:
            
            cents1 += 1
            remain +=1
   
    if (dollars != 0):
        print (dollars ,"x $1")
    if(cents25!=0):
        print (cents25,"x 25c")
    if (cents10 !=0):
        print (cents10,"x 10c")
    if (cents5 != 0):
        print (cents5,"x 5c")
    if (cents1 != 0):
        print (cents1,"x 1c")
    
    
        
    
                
    
