def change(paid, cost):
    coins = ['1c', '5c', '10c', '25c', '$1']
    coins = coins[::-1]
    values = [1, 5, 10, 25, 100]
    count = [0, 0, 0, 0, 0]
    
    q, r = 0, (paid - cost)
    for n, value in enumerate(reversed(values)):
        q, r = divmod(r, value)
        count[n] = q
    
    if sum(count):
        print('Your change is:')
    for n, coin in enumerate(count):
        if not coin:
            continue
        print(coin, 'x', coins[n])
        
def main():
    cost = int(input('Enter the cost (in cents):\n'))
    pay = 0
    while pay < cost:
        pay += int(input('Deposit a coin or note (in cents):\n'))
    change(pay, cost)

if __name__ == '__main__':
    main()