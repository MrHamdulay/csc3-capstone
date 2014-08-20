cost = eval(input('Enter the cost (in cents):\n'))
total_paid = 0

while total_paid < cost:
    pay = eval(input('Deposit a coin or note (in cents):\n'))
    total_paid += pay

total = total_paid - cost
change = [0] * 5
count = 0

coins = [100,25,10,5,1]

if total > 0:
    print("Your change is:")

for i in coins:
    change[count] = total // i
    total = total % i
    count += 1

count = 0

for i in change:
    if i:
        if count == 0:
            print(i,'x $1')
        else:
            print(i,'x', (str(coins[count]) + 'c'))
    count += 1
