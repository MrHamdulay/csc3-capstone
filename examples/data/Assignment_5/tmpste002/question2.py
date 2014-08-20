""" Calculate vending machine change """
__author__ = 'Stephen Temple - TMPSTE002'
__date__ = '2014/04/13'

cost = eval(input("Enter the cost (in cents):\n"))

amount = 0
while amount < cost:
    amount += eval(input("Deposit a coin or note (in cents):\n"))

change = amount - cost
if change > 0:
    print("Your change is:")
    if change >= 100:
        print(str(change // 100) + ' x $1')  # change // 100 is the number of $1 coins in the change amount
        change -= ((change // 100) * 100)  # decrease amount of change by number of $1 coins * 100 cents
    if change >= 25:
        print(str(change // 25) + ' x 25c')  # change // 25 is the number of 25c coins in the change amount
        change -= ((change // 25) * 25)  # decrease amount of change by number of 25c coins * 25 cents
    if change >= 10:
        print(str(change // 10) + ' x 10c')  # change // 10 is the number of 10c coins in the change amount
        change -= ((change // 10) * 10)  # decrease amount of change by number of 10c coins * 10 cents
    if change >= 5:
        print(str(change // 5) + ' x 5c')  # change // 5 is the number of 5c coins in the change amount
        change -= ((change // 5) * 5)  # decrease amount of change by number of 5c coins * 5 cents
    if change > 0:
        print(str(change) + ' x 1c')  # output remaining change in 1c coins