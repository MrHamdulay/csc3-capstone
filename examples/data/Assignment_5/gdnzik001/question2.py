"""Zikho Godana
15 April 2014
a program to simulate a vending machine and calculates change based on the amount paid"""

def vending():
    cost=eval(input("Enter the cost (in cents):\n"))
    if cost==0:
        return #the program stops if the entered cost is 0!
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    
    #ask the user for more money as long as the deposit is less than the cost
    while deposit<cost:
        deposit2=eval(input("Deposit a coin or note (in cents):\n"))
        deposit=deposit + deposit2
    change=deposit-cost 
    #but the change is given in coins and coins come in 1c,5c,10c,25c,$1
    change1=change//100
    change2=change-(change1*100)
    if change1!=0:
        print("Your change is:")
        print(change1,"x $1")   
        if change2>25:
            change3=change2//25
            print(change3,"x 25c")
            if deposit-(cost+((change1*100)+(change3*25)))!=0:
                change4=change2-(change3*25)
                print("1 x ",change4,"c",sep="")
                #print(change4)
        elif change2==25:
            print("1 x 25c")
    else:
        if change>25:
            print("Your change is:")
            change5=change//25
            print(change5,"x 25c")
            if change-(change5*25)!=0:
                change6=change-(change5*25)
                if change6%10==0:
                    print(change6//10,"x 10c")
            
        
    
 
vending()   