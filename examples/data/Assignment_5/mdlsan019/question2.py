'''A program that simulates a vending machine and calculates change based on the amount given
Sanele Mdlalose
14-04-2014
Assignment5,Question2'''

cost=eval(input("Enter the cost (in cents):\n"))
if cost !=0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    while cost>deposit:
        deposit2=eval(input("Deposit a coin or note (in cents):\n"))
        deposit+=deposit2
    
        
    change=deposit-cost
    if change>0:
        print("Your change is:")
        while change/100>=1: 
            mult_1a=int(change/100)
            change=change-(mult_1a*100)
            print(mult_1a,'x',"$1")
    
        while change/25>=1:
            mult_1b=int(change/25)
            change=change-(mult_1b*25)
            print(mult_1b,"x","25c")
        
        while change/10>=1:
            mult_1c=int(change/10)
            change=change-(mult_1c*10)
            print(mult_1c,'x','10c')
        
        while change/5>=1:
            mult_1d=int(change/5)
            change=change-(mult_1d*5)
            print(mult_1d,"x","5c")
        
        while change/1>=1:
            mult_1e=int(change/1)
            change=change-(mult_1e*1)
            print(mult_1e,'x','1c')    