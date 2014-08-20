cost= eval(input("Enter the cost (in cents):\n"))
if cost:
    deposit= eval(input("Deposit a coin or note (in cents):\n"))
    
    while (deposit<cost):
        deposit_added= eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=deposit_added
        
    change= deposit-cost
    cents=0
    
    if change!=0:
        print("Your change is:")
        if change>100:
            dollars= change//100
            print(dollars,"x $1")
            cents= change%100
            if (cents !=0) and (cents>=25):
                cents25=cents//25
                print(cents25,"x 25c")
                cents= cents%25 
                if (cents !=0) and (cents>=10):
                    cents10=cents//10
                    print(cents10,"x 10c")
                    cents= cents%10
                    if (cents !=0) and (cents>=5):
                        cents5= cents//5
                        print(cents5,"x 5c")
                        cents= cents%5
                        if (cents !=0) and (cents>=0):
                            cents1=cents
                            print(cents,"x 1c")
        elif change<100:
            cents=change   
            if (cents !=0) and (cents>=25):
                        cents25=cents//25
                        print(cents25,"x 25c")
                        cents= cents%25 
                        if (cents !=0) and (cents>=10):
                            cents10=cents//10
                            print(cents10,"x 10c")
                            cents= cents%10
                            if (cents !=0) and (cents>=5):
                                cents5= cents//5
                                print(cents5,"x 5c")
                                cents= cents%5
                                if (cents !=0) and (cents>=0):
                                    cents1=cents
                                    print(cents,"x 1c")            