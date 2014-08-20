#Axel du Plessis 14/04/2014
#Program used to calculate the change from a transaction

amount = eval(input("Enter the cost (in cents):\n"))

while amount>0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    amount -= deposit
    
change = amount*-1

symbol = ["$1","25c","10c","5c","1c"]

counter = 0

if change!=0:    
    print("Your change is:")
    
    for i in[100,25,10,5,1]:
        if change == 0:
            break
        else:
            if change//i == 0:
                counter += 1  
                continue
            else:
                print(str(change//i)+ " x " + symbol[counter])
                counter += 1    
                change %= i