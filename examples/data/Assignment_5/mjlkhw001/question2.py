# Vending machine
# Khwezi Majola
# MJLKHW001
# 14 April 2014

def ven():
    cost = int(input('Enter the cost (in cents):\n',))
    depo = 0
    while depo < cost:
        depo += int(input('Deposit a coin or note (in cents):\n'))
    change = depo - cost
    deno = ['$1', '25c', '10c', '5c', '1c']
    value = [100, 25, 10, 5, 1]
    if change > 0:
        print('Your change is:')
        for i in range(5):
            num = int(change/value[i])
            change -= (num) * value[i]
            if num > 0:
                print(str(num) + ' x ' + deno[i])
ven()