#calculating change when purchasing an item
#romelon chetty(chtrom001)
# 14 april 2014
#question2.py

denominations = [[100,'$1'], [25, '25c'], [10, '10c'], [5, '5c'], [1, '1c']] # list of denominations and values

cost = eval(input('Enter the cost (in cents):\n')) #input of cost of the item

now = 0

while now < cost:
    now += eval(input('Deposit a coin or note (in cents):\n'))

change = now - cost

if change != 0:
    print('Your change is:')

while (change != 0):
    for i in denominations:
        if change // i[0] == 0:
            continue
        else:
            print(change // i[0], 'x', i[1])
            change = change % i[0]
            break
            
