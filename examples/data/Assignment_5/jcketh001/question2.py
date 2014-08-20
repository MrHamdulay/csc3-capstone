'''program to simulate vending machine
ethan jackson
16 april 2014'''

#create inputs for the cost and deposit amounts
cost = eval(input("Enter the cost (in cents):\n"))
deposit = eval(input("Deposit a coin or note (in cents):\n"))
#the number of deposits needs to loop until cost is met/exceeded
while cost > deposit:
    deposit += eval(input("Deposit a coin or note (in cents):\n"))
    change = deposit - cost
    #to calculate number of 1$ coins integer divide the change by 100
    cents = change//100
    if(cents !=0):
        print("Your change is:\n"+str(cents),"x $1")
        change = change - 100*cents
        cents = change//25
    if (cents !=0):
        print(str(cents)+" x 25c")
        change = change - 25*cents
        cents = change//10
    if (cents !=0):
        print(str(cents)+"x 10c")
        change = change - 10*cents
        cents = change//5
    if (cents !=0):
        print(str(cents)+"x 5c")
        change = change - 5*cents
        cents = change//1
        print(str(cents)+"x 1c")
        
        
     
        
    
    
    