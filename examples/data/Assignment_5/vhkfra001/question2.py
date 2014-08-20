# Assignment 5
# Program to work out change
# Frans van Hoek
# 14 April 2014

payment = 0
cost = eval(input("Enter the cost (in cents):\n"))

while payment < cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    payment += deposit

# Work out the number of each coin
change = payment - cost
d1 = change // 100
change -= d1*100

c25 = change // 25
change -= c25*25

c10 = change // 10
change -= c10*10

c5 = change // 5
change -= c5*5

c1 = change // 1
change -= c1*1

# Now to print the change
if payment != cost: print('Your change is:')

if d1 != 0:
    print(d1,'x $1') 
if c25 != 0:
    print(c25, 'x 25c')
if c10 != 0:
    print(c10, 'x 10c')
if c5 != 0:
    print(c5, 'x 5c')
if c1 != 0:
    print(c1, 'x 1c')
    