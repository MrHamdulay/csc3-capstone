"""Vending Machine
Limpho Parkies
17-04-2014"""

cost=eval(input('Enter the cost (in cents):\n'))
if cost>0:
    money=eval(input('Deposit a coin or note (in cents):\n'))
    while money < cost:
        money+=eval(input('Deposit a coin or note (in cents):\n')) #changing the value of the input money
    change=money-cost 
    if change >0:
        print('Your change is:')
        if change>1:
            dollar= change//100
            change-=(dollar*100)
            if dollar>0:
                print(dollar,'x $1')
        if change>0:
            coins25=(change)//25
            change-=(coins25*25)
            if coins25>0:
                print(coins25,'x 25c')      
        if change>0:
            coins10=(change)//10
            change-=(coins10*10)
            if coins10>0:
                print(coins10,'x 10c')       
        if change>0:
            coins5=(change)//5
            change-=(coins5*5)
            if coins5>0:
                print(coins5,'x 5c')        
        if change>0:
            coins1=(change)//1
            if coins1>0:
                print(coins1,'x 1c')
     
        