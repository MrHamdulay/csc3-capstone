"""Vending Machine Change Calculator
Sbongakonke Mlangeni
16 April 2014"""

x = eval(input('Enter the cost (in cents):\n'))
if x == 0:
    print('')

if x != 0:
    y = eval(input('Deposit a coin or note (in cents):\n'))

while y<x:
    dy = eval(input('Deposit a coin or note (in cents):\n'))
    y += dy
           
a = y-x

if a != 0:
    print('Your change is:')
    if a >= 100:
        print(str(a//100) + ' x $1')
        a -= ((a//100) * 100)
    if a >= 25 and a < 100:
        print(str(a//25) + ' x 25c')
        a -= ((a//25) * 25)
    if a >= 10 and a < 25:
        print(str(a//10) + ' x 10c')
        a -= ((a//10) * 10)
    if a >= 5 and a < 10:
        print(str(a//5) + ' x 5c')
        a -= ((a//5) * 5)
    if a >= 1 and a < 10:
        print(str(a) + ' x 1c')
        
        
    
    
    