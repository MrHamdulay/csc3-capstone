cost=eval(input('Enter the cost (in cents):\n'))

ac=0

while ac < cost:
    pay=eval(input('Deposit a coin or note (in cents):\n'))
    ac=ac+pay
    
change = ac-cost  

if change != 0:
    print('Your change is:')
    
    dollar = change//100 

    if dollar > 0:
        print(dollar,'x $1')

    change = change%100
    twenty = change//25
    change = change%25        

    if twenty > 0:
        print(twenty,'x 25c')

    ten = change//10
    change = change%10            

    if ten >0:
        print(ten,'x 10c')

    five = change//5
    change=change%5                

    if five != 0:
        print(five,'x 5c')

    one=change//1

    if one != 0:
        print(one,'x 1c')