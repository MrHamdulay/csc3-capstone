
def vending_machine():
    money=0
    cost=int(input("Enter the cost (in cents):\n"))
    #print(cost)
    while money < cost: 
        new=int(input("Deposit a coin or note (in cents):\n"))
        money=money+new
        #print(money)
    
    #Make change
    change=money-cost
    if change>0:
        print("Your change is:")
    while change > 0:
        if change >= 100:
            dollar=change//100
            change=change-dollar*100
            #print (change)
            print (dollar, "x $1")
        elif change>= 25:
            quarter=change//25
            change=change-quarter*25
            #print(change)
            print(quarter, "x 25c")
        elif change>=10:
            dime=change//10
            change=change-dime*10
            #print(change)
            print (dime, "x 10c")
        elif change>=5:
            nickle=change//5
            change=change-nickle*5
            print(nickle, "x 5c")
        else:
            penny=change//1
            print(penny, "x 1c")
            change=change-penny*1
        
    #print(change)
vending_machine()
    