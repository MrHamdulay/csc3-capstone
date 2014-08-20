# a program that determines the change to give in a vending machine
#Jenny Luo
#15 april 2014

#get the input from user 
cost=eval(input("Enter the cost (in cents):\n"))

#get the payment from user and calculate total payments
if cost>0:
    total=eval(input("Deposit a coin or note (in cents):\n"))
    
    payment=0
    while total < cost:
        payment=eval(input("Deposit a coin or note (in cents):\n"))
        total=payment+total

#determine the change in terms of various "coins" (i.e. $1,25c,etc.)
    
    change=total-cost
    coin=0
    if change>0:
        print("Your change is:")
    if change>=100:                 
        coin=change//100
        change=change%(coin*100)
        print(coin,"x","$1")
    if change>=25:
        coin=change//25
        change=change%(coin*25)
        print(coin,"x","25c")
    if change>=10:
        coin=change//10
        change=change%(coin*10)
        print(coin,"x","10c")
    if change>=5:
        coin=change//5
        change=change%(coin*5)
        print(coin,"x","5c")
    if change>=1:
        coin=change//1
        change=change%(coin*1)
        print(coin,"x","1c")
    
    
    


    
    
    