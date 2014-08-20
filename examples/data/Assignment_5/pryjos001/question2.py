"""Vending machine simulator
Joe Preyer
16 April 2014"""

# Ask for cost
cost = eval(input("Enter the cost (in cents):\n"))

# Get deposit from user (in cents), subtract from remaining cost and if difference is positive, ask for another deposit
diff = cost
while diff > 0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    diff -= deposit

# When difference is negative, divide it into certain denominations
diff*=-1 #Makes diff positive for manipulation
dollar = diff//100
quarter = (diff%100)//25
ten = (diff%25)//10
five = ((diff%25)%10)//5
one = (diff%5)

#Allocate change to user

if diff>0:
    print ("Your change is:")

if dollar>0:
    print (dollar, "x $1")
if quarter>0:
    print (quarter, "x 25c")
if ten>0:
    print (ten, "x 10c")
if five>0:
    print (five, "x 5c")
if one>0:
    print (one, "x 1c")
