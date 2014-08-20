
cost=eval(input("Enter the cost (in cents):\n"))
if cost>0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    while deposit<cost:
        additional=eval(input("Deposit a coin or note (in cents):\n"))
        deposit=deposit+additional
    

    if deposit>cost: 
        change=deposit-cost
        print("Your change is:")
        if change//100>0:
            count100=change//100
            change=change-(count100*100)
            print(count100, "x $1")
        if change//25>0:
            count25=change//25
            change=change-(count25*25)
            print(count25, "x 25c")
        if change//10>0:
            count10=change//10
            change=change-(count10*10)
            print(count10, "x 10c")
        if change//5>0:
            count5=change//5
            change=change-(count5*5)
            print(count5, "x 5c")
        if change//1>0:
            count1=change//1
            print(count1, "x 1c")
            

            

    
    
    
        
    
    
        
    