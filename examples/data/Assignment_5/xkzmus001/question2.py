"""question2.py Vending Machine
Author : Musa Xakaza
Student# : XKZMUS001
Date : 12/04/2014"""

def getCoins(rem):
    sChange = ''
    for coin in [100,25,10,5,1]:
        q = rem//coin
        if q != 0:
            sChange += str(q)+' x '
            if coin != 100: sChange += str(coin)+'c\n'
            else : sChange += '$1\n'
            rem %= coin
            if rem == 0: break
    return sChange[:-1:]   

def main():
    cost = eval(input('Enter the cost (in cents):\n'))
    deposit = 0
    while not deposit >= cost:
        deposit += eval(input('Deposit a coin or note (in cents):\n'))
    if (deposit - cost) > 0: print('Your change is:\n'+getCoins(deposit - cost))
    else: pass#print('No change')

main()