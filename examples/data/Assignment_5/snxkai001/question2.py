#kairav soni change

price=eval(input("Enter the cost (in cents):\n"))

amount=0


while (amount)<(price):
    amount+=eval(input("Deposit a coin or note (in cents):\n"))
    
    
Rchange=(amount)-(price)


if Rchange==0:
    print("")
    
    
else:
    dollars=(Rchange//100)
    if dollars>0:
        Rchange -= (dollars*100)
        
    
    quarters=(Rchange//25)
    if quarters>0:
        Rchange -= (quarters*25)
        
        
    
    dimes=(Rchange//10)
    if dimes>0:
        Rchange -=(dimes*10)
        
        
    
    nickels=(Rchange//5)
    if nickels>0:
        Rchange -=(nickels*5)
        
    
    pennies=(Rchange//1)
    
    
    print("Your change is:")
    
    
    if dollars>0:
        print(dollars, "x $1")
        
        
    if quarters>0:
        print(quarters, "x 25c")
        
        
    if dimes>0:
        print(dimes, "x 10c")
        
        
    if nickels>0:
        print(nickels, "x 5c")
        
        
    if pennies>0:
        print(pennies, "x 1c")
    
    
    
    
