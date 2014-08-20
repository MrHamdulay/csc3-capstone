#Calculating change in a vending machine
#Lauren de Bruyn
#16 April 2014
cost=eval(input("Enter the cost (in cents): \n"))
while cost>0:
    deposit=eval(input("Deposit a coin or note (in cents): \n"))
    cost=cost-deposit
change=-1*cost

#Converting change into dollars,quarters,nickels,dimes and pennies
if change>0:
    print("Your change is:")
    dollars=int(change/100)
    if dollars>0:
        print(dollars,"x $1")
        
    change=change-dollars*100
    
    quarters=int(change/25)
    if quarters>0:
        print(quarters,"x 25c")        
    
    change=change-quarters*25
    
    dimes=int(change/10)
    if dimes>0:
        print(dimes, "x 10c")
    
    change=change-dimes*10
    
    nickels=int(change/5)
    if nickels>0:
        print(nickels,"x 5c")
        
    change=change-nickels*5
    
    pennies=int(change)
    if pennies>0:
        print(pennies,"x 1c")
    
        
    


