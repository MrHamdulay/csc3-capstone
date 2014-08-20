"""Vending MAchine
Yusuf Khan
17 April 2014"""

cost = eval(input('Enter the cost (in cents):\n'))
paid = 0
while cost > paid:
    paid += eval(input('Deposit a coin or note (in cents):\n'))
        
change = paid - cost
change_wallet = [0,0,0,0,0]
if change != 0:
    while change >= 100:
        change_wallet[0] += 1
        change -= 100
    while change >= 25:
        change_wallet[1] += 1
        change -= 25
    while change >= 10:
        change_wallet[2] += 1
        change -= 10
    while change >= 5:
        change_wallet[3] += 1
        change -= 5
    while change >= 1:
        change_wallet[4] += 1
        change -= 1
            
    print('Your change is:')
    if change_wallet[0] > 0:
        print(str(change_wallet[0]) + ' x ' + '$1')
    if change_wallet[1] > 0:
        print(str(change_wallet[1]) + ' x ' + '25c')
    if change_wallet[2] > 0:
        print(str(change_wallet[2]) + ' x ' + '10c') 
    if change_wallet[3] > 0:
        print(str(change_wallet[3]) + ' x ' + '5c')
    if change_wallet[4] > 0:
        print(str(change_wallet[4]) + ' x ' + '1c')      