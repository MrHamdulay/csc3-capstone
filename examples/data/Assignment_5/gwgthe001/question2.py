#A program to simulate a vending machine and calculate change based on the amount paid
#Thembekani Gwegwana
#April 2014

def machine():
    cost=0
    deposit=0
    change=0
    cost=eval(input('Enter the cost (in cents):\n'))
    if cost>0:
        deposit=eval(input('Deposit a coin or note (in cents):\n'))
    while cost>deposit:
        #deposit=eval(input('Deposit a coin or note (in cents):\n'))
        second_deposit=eval(input('Deposit a coin or note (in cents):\n'))
        deposit+=second_deposit
    
    change=deposit-cost
    if change>0:
        print('Your change is:')
    #calculating the change
        dollars=change//100 
        change=change-dollars*100
        _25c=change//25
        change=change-_25c*25
        _10c=change//10
        change=change-_10c*10
        _5c=change//5
        change=change-_5c*5
        _1c=change
    #Printing the change
        if dollars>0:
            print(dollars,'x','$1')
        if _25c>0:
            print(_25c,'x','25c')
        if _10c>0:
            print(_10c,'x','10c')
        if _5c>0:
            print(_5c,'x','5c')
        if _1c>0 :
            print(_1c,'x','1c') 
machine()
