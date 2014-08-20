"""Reece Gounden
Assignment 5 Q2
"""

def calchange(change, cval):
    count = 0
    while change // cval != 0:
        count += 1
        change -= cval
    return count
    

cost = eval(input("Enter the cost (in cents):\n"))
total = 0
while cost > total:
    total = total + eval(input('Deposit a coin or note (in cents):\n'))

change = total - cost

if change != 0:
    print('Your change is:')
    for i in [100, 25, 10, 5, 1]:
        countcoin = calchange(change,i)
        change = change - countcoin*i
        
        if (i == 100) and (countcoin > 0):
            print(str(countcoin),'x $1')
        elif countcoin != 0:
            print(str(countcoin),'x',str(i)+'c')
        