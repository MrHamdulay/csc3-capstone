item_cost=eval(input('Enter the cost (in cents):\n'))

if item_cost>0:
    intialpayment=eval(input('Deposit a coin or note (in cents):\n'))

    while intialpayment<item_cost:
        intialpayment+=eval(input('Deposit a coin or note (in cents):\n'))
       
        
    
    if item_cost<intialpayment:
        change_1=intialpayment-item_cost
        if change_1!=0:
            print('Your change is:')
        dollars=change_1//100
        
        if change_1!=0:
            if change_1>100:
                 
                print(dollars,'x $1')
        cent25=(change_1-dollars*100)//25
        if cent25!=0:
            print(cent25,'x 25c')
        cent10=(change_1-dollars*100-cent25*25)//10
        if cent10!=0:
            print(cent10,'x 10c')
        cent5=(change_1-dollars*100-cent25*25-cent10*10)//5
        if cent5!=0:
            print(cent5,'x 5c')
        cent1=(change_1-dollars*100-cent25*25-cent10*10-cent5*5)
        if cent1!=0:
            print(cent1,'x 1c')