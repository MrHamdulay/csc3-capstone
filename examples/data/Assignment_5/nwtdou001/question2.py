coins = [100,25,10,5,1]
coin_names = '$1 25c 10c 5c 1c'
chg_coins = [0,0,0,0,0]

cost = eval(input('Enter the cost (in cents):\n'))
dep = 0
while dep<cost:
    dep = dep + eval(input('Deposit a coin or note (in cents):\n'))


chg = dep-cost

if chg>0:
    print('Your change is:')
    
    for i in range(len(coins)):
        chg_coins[i] = chg//coins[i]
        chg %= coins[i]
        
    for i in range(len(chg_coins)):
        if chg_coins[i]!=0:
            print(chg_coins[i],'x',coin_names.split(' ')[i])