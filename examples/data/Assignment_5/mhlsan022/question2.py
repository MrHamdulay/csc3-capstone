'''Let's make a vending machine simulation program and it should calculate change based on the amount paid.
Sandile Mahlangu
14 April 2014'''

def vendor():
    '''Vending Machine payment and change'''
    cost=eval(input('Enter the cost (in cents):\n'))
    
    deposit=0
    while deposit<cost: #When the money deposited is not enough
        more=eval(input('Deposit a coin or note (in cents):\n'))
        deposit+=more
    else:#When we have enough money
        change=deposit-cost
        one_dollar=change//100
        left=change%100
        twenty_five_cents=left//25
        left2=left%25
        ten_cents=left2//10
        left3=left2%10
        five_cents=left3//5
        left4=left3%5
        one_cents=left4//1
        if one_dollar>0 or twenty_five_cents>0 or ten_cents>0 or five_cents>0 or one_cents>0:
            print('Your change is:')
        if one_dollar>0:
            print(one_dollar,'x $1')
        if twenty_five_cents>0:
            print(twenty_five_cents,'x 25c')
        if ten_cents>0:
            print(ten_cents,'x 10c')
        if five_cents>0:
            print(five_cents,'x 5c')
        if one_cents>0:
            print(one_cents,'x 1c')
        
vendor()