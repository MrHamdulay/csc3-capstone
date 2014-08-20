#ass.5 Q2    -   Vending Machine
#Kavir Ranchod   -   rnckav001
#16/04/2014

cost = eval(input("Enter the cost (in cents):\n"))
deposit1 = eval(input("Deposit a coin or note (in cents):\n"))
while deposit1<cost:
    deposit1 += eval(input("Deposit a coin or note (in cents):\n"))
change=deposit1-cost
if change>0:
    print("Your change is:")
if change >= 100:
    hundreds=change//100
    change-=hundreds*100
    if hundreds >=1:
        print(hundreds,"x $1")    
if change >= 25:
    quarters=change//25
    change-=25*quarters
    if quarters >=1:
        print(quarters,"x 25c")    
if change >= 10:
    tens=change//10
    change-=10*tens
    if tens >=1:
        print(tens,"x 10c")    
if change >= 5:
    fives=change//5
    change-=5*fives
    if fives >=1:
       print(fives,"x 5c")    
if change >= 1:
    ones=change//1
    if ones >=1:
        print(ones,"x 1c")    
