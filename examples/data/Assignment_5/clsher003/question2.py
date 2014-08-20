"""vending machine program
herman claassens
14 april 2014"""

# prompt user for cost and deposits
cost=eval(input("Enter the cost (in cents):\n"))
deposit=eval(input("Deposit a coin or note (in cents):\n"))

if cost==deposit:
    True
    x=-1
    y=-1
    z=-1
    r=-1
    p=-1 # variables to serve as loop repeat counters
elif deposit<cost:
    while deposit<cost:
        #ask for deposit until deposits exceeds cost
            next_deposit=eval(input("Deposit a coin or note (in cents):\n"))
            deposit+=next_deposit
    change=deposit-cost

    if change==0:
        True
    x=0 #100c
    while change-100>=0 :
        new_change=change-100
        change=new_change
        x+=1
   
    y=0 #25c
    while change-25>=0:
            new_change=change-25
            change=new_change
            y+=1 
   
    z=0 #10c
    while change-10>=0:
            new_change=change-10
            change=new_change
            z+=1  
    
    r=0 #5c
    while change-5>=0:
        new_change=change-5
        change=new_change
        z+=1  
      
    p=0 #1c
    while change-1>=0:
            new_change=change-1
            change=new_change
            p+=1 
    
    
elif deposit>cost:
    change=deposit-cost
    x=0 #100c
    while change-100>=0 :   
        new_change=change-100
        change=new_change
        x+=1
 
    y=0 #25c
    while change-25>=0:
        new_change=change-25
        change=new_change
        y+=1 
       

    z=0 #10c
    while change-10>=0:
        new_change=change-10
        change=new_change
        z+=1  
     
        
    r=0 #5c
    while change-5>=0:
        new_change=change-5
        change=new_change
        r+=1  
     
          
    p=0 #1c
    while change-1>=0:
        new_change=change-1
        change=new_change
        p+=1     
    
# use loop counters 
if x>0 or y>0 or z>0 or r>0 or p>0:
    print("Your change is:")
if x>0:
    print(x,"x $1")
if y>0:
    print(y,"x 25c")
if z>0:
    print(z,"x 10c")
if r>0:
    print(r,"x 5c")
if p>0:
    print(p,"x 1c")  
