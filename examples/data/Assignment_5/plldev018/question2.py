#VendingMachine
#Devaksha Pillay
#15 April 2014

#function to determine change
def paid():
    price = input ("Enter the cost (in cents):\n")
    price = eval (price) 
    
    if price!=0:  
        payment = input("Deposit a coin or note (in cents):\n")
        payment = eval (payment)
    
        if payment>=price:
            change = payment - price
            return change
    
        #continue until money paid is more than the cost of the item
        while payment<price:
            more_money = input("Deposit a coin or note (in cents):\n")
            more_money = eval(more_money)
            payment = payment + more_money
            if payment>=price:
                change = payment - price
                return change
            else:
                continue
    
change = paid()
per_denomination = 0
if change !=None:
    
    
    #for each available denomination - goes through a loop with all available denominations which are smaller
    if change>100:
        print("Your change is:")
        per_denomination = change//100
        print(per_denomination, "x $1")
        per_denomination = per_denomination*100
        change = change - per_denomination
        if change>0:
            per_denomination = change//25
            print(per_denomination, "x 25c")
            per_denomination = per_denomination*25
            change = change-per_denomination
            if change>0:
                per_denomination = change//10
                print(per_denomination, "x 10c")
                per_denomination = per_denomination*10
                change = change - per_denomination        
                if change>0:
                    per_denomination = change//5
                    print(per_denomination, "x 5c")
                    per_denomination = per_denomination*5
                    change = change - per_denomination
                    if change>0:
                        print(change, "x 1c")
    elif change>=25:
        print("Your change is:")
        per_denomination = change//25
        print(per_denomination, "x 25c")
        per_denomination = per_denomination*25
        change = change-per_denomination
        if change>0:
                per_denomination = change//10
                print(per_denomination, "x 10c")
                per_denomination = per_denomination*10
                change = change - per_denomination        
                if change>0:
                        per_denomination = change//5
                        print(per_denomination, "x 5c")
                        per_denomination = per_denomination*5
                        change = change - per_denomination
                        if change>0:
                            print(change, "x 1c")
    elif change>=10:
        print("Your change is:")
        per_denomination = change//10
        print(per_denomination, "x 10c")
        per_denomination = per_denomination*10
        change = change - per_denomination
        if change>0:
            per_denomination = change//5
            print(per_denomination, "x 5c")
            per_denomination = per_denomination*5
            change = change - per_denomination
            if change>0:
                print(change, "x 1c")        
    elif change>=5:
        print("Your change is:")    
        per_denomination = change//5
        print(per_denomination, "x 5c")
        per_denomination = per_denomination*5
        change = change - per_denomination
        if change>0:
            print(change, "x 1c")
    elif change>=1:
        print("Your change is:")
        print(change, "x 1c")