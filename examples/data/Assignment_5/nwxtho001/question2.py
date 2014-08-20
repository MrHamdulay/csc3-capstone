'''Vending Machine Simulator
Like Goat Simulator but worse'''

coins = ['$1', '25c', '10c', '5c', '1c']
values = [100, 25, 10, 5, 1]

cost = eval (input ('Enter the cost (in cents):\n'))

if cost != 0:

    paid = eval (input ('Deposit a coin or note (in cents):\n'))
    
    while paid < cost:
        paid += eval (input ('Deposit a coin or note (in cents):\n'))
    
    change = paid - cost
    
    if change != 0:
        print ('Your change is:')
        for value in values:
            count = 0
            index = values.index (value)
            coin = coins [index]
            while change >= value:
                change -= value
                count += 1
            if count != 0:
                print (count, 'x', coin)