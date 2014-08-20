#Assignment5 Question2
#MDLCar002
#VendingMachine


cost=eval(input("Enter the cost (in cents):\n"))
paid=0

while (cost>paid):
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    paid=paid+deposit

change=paid-cost
if (change>0):
    print("Your change is:")
    #$1
    if((change//100)>0):
        print((change//100),"x $1")
        change=change-(100*(change//100))

    #25c
    if((change//25)>0):
        print((change//25),"x 25c")
        change=change-(25*(change//25))
            
    #10c
    if((change//10)>0):
        print((change//10),"x 10c")
        change=change-(10*(change//10))
                
    #5c
    if((change//5)>0):
        print((change//5),"x 5c")
        change=change-(5*(change//5))
                    
    #1c
    if((change//1)>0):
        print((change//1),"x 1c")
        change=change-(1*(change//1))