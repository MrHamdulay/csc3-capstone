#Question 2
#Adam Rosendorff-RSNADA001
#15/04/2014

coin_name = ['$1','25c','10c','5c','1c']
coins = [100,25,10,5,1]
number_returned = [0,0,0,0,0]
cost = eval(input('Enter the cost (in cents):\n'))
paid = 0
while (paid < cost):
    paid += eval(input('Deposit a coin or note (in cents):\n'))
change = paid - cost

if change != 0:
    print('Your change is:')
for i in range(5):
    while (change >= coins[i]):
        number_returned[i] += 1
        change -= coins[i]
    if number_returned[i] > 0:
        print(number_returned[i],'x',coin_name[i])
        
