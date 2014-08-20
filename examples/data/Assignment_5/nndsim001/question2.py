# This program simulates a vending machine and calculate change based on the amount paid.
# Given the cost, the user should first be prompted to add more money until the cost is 
# met/exceeded by the payment.
# It is assume that all change is given in coins only 
# and coins come in the following denominations: 1c, 5c, 10c, 25c, $1

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 15 April 2014


# values printed on the coins
coins = ["1c","5c","10c","25c","$1"]

# values of coins in cents
coincents = ("1","5","10","25","100")


# Ask user to enter the cost price of the item
costprice = eval(input("Enter the cost (in cents):\n"))
change = 0
total = 0

# This loops ask the user to enter an amount they want to pay with
while total < costprice:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    total += deposit

change = total - costprice # variable to store the change
div = 0 # variable to store the division value
p = 4 # index position in the cents string

if change != 0: print("Your change is:")

# This loop calculates the change
while change != 0:
    if change//int(coincents[p]) != 0: # ensures that the change is not zero
        div = change//int(coincents[p]) # change divisible by cents
        print(div,"x",coins[p]) # display the value of the computation above
    change -= div*int(coincents[p]) # decrease the change
    p -= 1 # decrease the index position  



# Sample I/O:

# Enter the cost (in cents):
# 750
# Deposit a coin or note (in cents):
# 500
# Deposit a coin or note (in cents):
# 500
# Your change is:
# 2 x $1
# 2 x 25c