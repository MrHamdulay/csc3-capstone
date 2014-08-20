#simulating a vending machine
#Kayla Hendricks
#16 April 2014

cost = eval(input("Enter the cost (in cents):\n"))
start = 0                   #starting with 0c
            
while start<cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    start+=deposit          #making start equal to coins/notes deposited
    
change = start-cost

if change!=0:               #if you have deposited more money than your item costs
    print("Your change is:")
    while (change-100)>=0:
        amount= change//100
        print(amount,"x $1")
        change-=100*amount     #your change less the appropriate number of dollars returned
    while (change-25)>=0:
        amount= change//25
        print(amount,"x 25c")
        change-=25*amount      #your change less the appropriate number of 25c returned
    while (change-10)>=0:
        amount= change//10
        print(amount,"x 10c")
        change-=10*amount      #your change less the appropriate number of 10c returned
    while (change-5)>=0:
        amount= change//5
        print(amount,"x 5c")
        change-=5*amount       #your change less the appropriate number of 5c returned
    while (change-1)>=0:
        print(change,"x 1c")
        change=0                #so that loop does not begin again
        
        
        
        
    