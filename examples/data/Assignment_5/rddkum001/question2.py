"""Calculating change from a vending machine
Kumaran Reddy
16 April 2014"""

#Stipulate the amounts that can be used
denominations = [[100, '$1'], [25, '25c'], [10, '10c'], [5, '5c'], [1, '1c']]
cost=eval(input("Enter the cost (in cents):\n"))
paid=0
#To ensure user deposits more moeny than actual cost
while paid < cost:
    paid+=eval(input("Deposit a coin or note (in cents):\n"))
change=paid-cost
#Give change in denominations
if change != 0:
    print("Your change is:")
    while change != 0:
        for i in denominations:
            if change//i[0] == 0:
                continue
            else:
                print(change//i[0],'x',i[1],sep=' ')
                change=change%i[0]
                break
            