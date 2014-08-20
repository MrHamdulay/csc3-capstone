__author__ = 'George de Kock'
#2014-04-13
cost = eval(input("Enter the cost (in cents):\n"))
paid = 0
while paid < cost:
    paid += eval(input("Deposit a coin or note (in cents):\n"))
change = paid-cost
dollar, tfive, ten, five, one = 0,0,0,0,0
while change >= 100:
    dollar += 1
    change -= 100
while change >= 25:
    tfive += 1
    change -= 25
while change >= 10:
    ten += 1
    change -= 10
while change >= 5:
    five += 1
    change -= 5
while change >= 1:
    one += 1
    one -= 1
if paid-cost !=0:
    print("Your change is:")
if dollar != 0:
    print(dollar,"x $1")
if tfive != 0:
    print(tfive,"x 25c")
if ten != 0:
    print(ten,"x 10c")
if five != 0:
    print(five,"x 5c")
if one != 0:
    print(one,"x 1c")