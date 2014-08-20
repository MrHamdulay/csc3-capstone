x=eval(input("Enter the cost (in cents):\n")) #prompt user for amount
if x !=0:     
    y=eval(input("Deposit a coin or note (in cents):\n"))
    while y<x:
        z=eval(input("Deposit a coin or note (in cents):\n"))
        y=y+z #increase value of y by next input if initial input isnt greater than x (and loop continues while y is smaller than x
    
    change=y-x #input-price #1,5,10,25,1
    if change != 0:
        print("Your change is:")
    if (change/100)>=1:
        print(int(change/100), "x $1") #hhow many 100c needed 
    if ((change%100)/25)>=1:
        print(int((change%100)/25), "x 25c") #how many 25c needed
    if (((change%100)%25)/10)>=1:
        print(int((((change%100)%25)/10)), "x 10c") #how many 10c needed
    if ((((change%100)%25)%10)/5)>=1:
        print(int((((change%100)%25)%10)/5), "x 5c")  #how many 5c needed
    if ((((change%100)%25)%10)%5)!=0:
        print(((((change%100)%25)%10)%5), "x 1c")  #how many 1c needed
