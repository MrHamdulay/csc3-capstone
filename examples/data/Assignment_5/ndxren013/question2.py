
n = eval(input('Enter the cost (in cents):\n'))#input

paid = 0

while paid < n:
    paid += eval(input('Deposit a coin or note (in cents):\n'))#evaluating cost

change = paid - n

if change > 0:
    print('Your change is:')

coins = 0
while change >= 100: #working out change 
    change -= 100
    coins += 1
if coins > 0:
    print(coins, 'x', '$1')

coins = 0
while change >= 25:
    change -= 25
    coins += 1
if coins > 0:
    print(coins, 'x', '25c')

coins = 0
while change >= 10:
    change -= 10
    coins += 1
if coins > 0:
    print(coins, 'x', '10c')

coins = 0
while change >= 5:
    change -= 5
    coins += 1
if coins > 0:
    print(coins, 'x', '5c')

coins = 0
while change >= 1:
    change -= 1
    coins += 1
if coins > 0:
    print(coins, 'x', '1c')
