# Vending machine program
# By Nasreen
import math

#ask user for cost
cost = eval(input('Enter the cost (in cents):\n'))
d = 0
a = 0

#ask user for money
while a < cost:
    d = eval(input('Deposit a coin or note (in cents):\n'))
    a = a + d
change = (a - cost)#calculates change

#gives user change
if change != 0:
    print('Your change is:')

    if 100 <= change:
        c = change//100
        print(c, 'x $1', sep=' ')
        change = change - (c*100)
    if (change <100) and (25 <= change):
        b = change//25
        print(b, 'x 25c', sep =' ')
        change = change -(b*25)
    if (change < 25) and (10 <= change):
        y = change//10
        print(y, 'x 10c', sep=' ')
        change = change -(y*10)
       
    if (change < 10) and (5 <= change):
        z = change//5
        print(z, 'x 5c', sep=' ')
        change = change -(z*5)
    if change != 0:    
        print(change, 'x 1c', sep=' ')
                                            