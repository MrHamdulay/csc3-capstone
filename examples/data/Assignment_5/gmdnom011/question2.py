# Program to simulate a vending machine and to calculate change
# Nomsa Gamedze
# 14 April 2014

def vending_machine():
    cost = eval(input("Enter the cost (in cents):"'\n'))
    while cost  > 0:
        payment = eval(input("Deposit a coin or note (in cents):"'\n'))
        cost -= payment
    change = cost*-1
    dollars = change//100
    after_dollars = change%100
    quarters = after_dollars//25
    after_quarters = after_dollars%25
    dimes = after_quarters//10
    after_dimes = after_quarters%10
    nickels = after_dimes//5
    cents = after_dimes%5
    coins = ""
    if dollars:
        coins += str(dollars) + " x $1" + '\n'
    if quarters:
        coins += str(quarters) + " x 25c" + '\n'
    if dimes:
        coins += str(dimes) + " x 10c" + '\n'
    if nickels:
        coins += str(nickels) + " x 5c" + '\n'
    if cents:
        coins += str(cents) + " x 1c" + '\n'
    if coins:
        print("Your change is:", coins, sep='\n')
        
vending_machine()