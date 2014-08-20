"""program to calculate change from a vending machine
yasha longstaff
15 april 2014"""

cost = eval(input ('Enter the cost (in cents):\n'))
m = 0
while m < cost:
    deposit = eval(input('Deposit a coin or note (in cents):\n'))
    m += deposit
change = m - cost
    
if change > 0:
    print ('Your change is:')
dollar = change //100
change = change - dollar*100
cents25 = change%100//25
change = change - cents25*25
cents10 = change//10
change = change - cents10*10
cents5 = change//5
change = change - cents5*5
cents1 = change//1
change = change - cents1*1

if dollar >0:
        print(dollar, 'x $1')
if cents25> 0:
        print (cents25, 'x 25c')
if cents10 > 0:
        print (cents10, 'x 10c')
if cents5 > 0:
        print(cents5, 'x 5c')
if cents1 > 0:
        print (cents1, 'x 1c')




