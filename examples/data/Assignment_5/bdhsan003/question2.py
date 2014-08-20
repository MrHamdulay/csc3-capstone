
#bdhsan003

cos=eval(input("Enter the cost (in cents):\n"))
tot = 0
#set to 0

while tot < cos: 
    dep=eval(input("Deposit a coin or note (in cents):\n"))
    tot += dep 
    
else:
    
    #Chnge is needed when tot>cost
    
    chnge = tot - cos
    if chnge != 0:
        print("Your change is:")
    rem = chnge
    
    #classify chnge into diff coins
    
    Amt_left=chnge//100
    if Amt_left !=0:
        print(str(Amt_left)+ ' x $1')
        rem = chnge - Amt_left*100
        
    if rem != 0:
        Amt_left = rem//25
        if Amt_left !=0:
            print(str(Amt_left)+ ' x 25c')
            rem = rem - Amt_left*25
            
    if rem != 0:
        Amt_left = rem//10
        if Amt_left !=0:
            print(str(Amt_left)+ ' x 10c')
            rem = rem - Amt_left*10 
            
    if rem != 0:
        Amt_left = rem//5
        if Amt_left !=0:
            print(str(Amt_left)+ ' x 5c')
            rem = rem - Amt_left*5 
            
    if rem != 0:
        Amt_left = rem//1
        if Amt_left !=0:
            print(str(Amt_left)+ ' x 1c')
            rem = rem - Amt_left*1    
            
        
    
        
        
         
        
    
           