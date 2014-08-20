"""the program simulates the vending machine and calculate change based on the amount paid
Hebert Tema- TMXTHA006
15 April 2014"""
    

#get the cost and the deposit
cost=eval(input("Enter the cost (in cents):\n"))
if cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))

    #get more deposit until the total deposit is equal or more than the cost
    while deposit<cost:                                          
        deposit+=eval(input("Deposit a coin or note (in cents):\n"))
    
    #create list for coins and for results from functions
    results=[100, 25, 10, 5, 1]
    coins=["$1", "25c", "10c", "5c", "1c"]
    quantity=[]
    
    #calculate the change from input(cost and deposit)
    change=deposit-cost
    
    #divide the change into coins
    j=0 #where j is an index
    while change>0:
        no_coins=change//results[j]     #no_coins represents number of coins
        change=change-(no_coins*results[j])    #new change=curent change-value of coins
        
        if no_coins==0:
            results.remove(results[j])      #remove the coin on the two list if it cannont be in the change, "FOR LEAST POSSIBLE NUMBER OF COINS"
            coins.remove(coins[j])         
        
        elif change==0:
            results=results[:j+1]
            coins=coins[:j+1]
            quantity.append(no_coins)      #END OF LOOP. the terminating coin is in the change
            
              
        else: 
            quantity.append(no_coins)
            j+=1   

    #output the change
    if quantity:
        print("Your change is:")
        for i in coins:
            print(quantity[coins.index(i)], "x", i)   #coins.index(i) returns an index of i, element of coins, which is equal to the index of the corresponding number of coins