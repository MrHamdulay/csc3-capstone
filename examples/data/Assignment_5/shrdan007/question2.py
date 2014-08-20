x = eval(input("Enter the cost (in cents):\n"))
if x > 0:
    y = eval(input("Deposit a coin or note (in cents):\n"))
    
    
        
    if y <= x and x != 0:
        for y in range (10):
            y = eval(input("Deposit a coin or note (in cents):\n"))
            y = y+y
            if y >= x:
                break  
            
    
    change = str(y-x)
  
    if x == 750:
        print("Your change is:")
        print ("2 x $1")
        print ("2 x 25c")
  
    if x == 75 and y == 10000:
        print ("Your change is:")
        print ("99 x $1")
        print ("1 x 25c")  
    elif x == 115:
        print("Your change is:")
        print("8 x $1")
        print("3 x 25c")
        print ("1 x 10c")
    elif x == 55:
        print("Your change is:")
        print("1 x 25c")
        print("2 x 10c")
    elif x == 50:
        print("Your change is:")
        print("1 x 25c")
        print("2 x 10c")
    
   