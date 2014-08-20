"""Charlie Shang
Assignment 5 Q2
Vending Machine 15 april 2014"""

def calcchange(change, CoinValue):
    count = 0
    while change // CoinValue != 0: #divide the change amount by the coin denomination until no further coins can be extracted from the change amount
        count += 1 #count of the coin
        change -= CoinValue #subtract the amount from the change
    return count
    

cost = eval(input("Enter the cost (in cents):\n"))
total = 0
while cost > total: #deposit until enough cash is received
    total = total + eval(input('Deposit a coin or note (in cents):\n'))

change = total - cost

if change != 0: #only execute the code if there is change
    print('Your change is:')
    for i in [100, 25, 10, 5, 1]: #start with the biggest denomination coin
        countcoin = calcchange(change, i)
        change = change - countcoin * i
        
        if (i == 100) and (countcoin > 0):
            print(str(countcoin), 'x $1') #if the con value is 100c, print $1
        elif countcoin != 0: #for all other coins
            print(str(countcoin), 'x', str(i) + 'c')
        