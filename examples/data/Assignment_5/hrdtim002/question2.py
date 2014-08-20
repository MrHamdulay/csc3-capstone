"""Vending Machine
Tim Hardie
16-4-14"""

def calc_change (remaining):
    # calculating the different number of each coin
    num_dollars = remaining//100
    remaining %= 100
    num_25c = remaining//25
    remaining %= 25
    num_10c = remaining//10
    remaining %= 10
    num_5c = remaining//5
    remaining %= 5
    num_1c = remaining
    
    # printing how many of each coin will be required
    if num_dollars: print(num_dollars, "x $1")
    if num_25c: print(num_25c, "x 25c")
    if num_10c: print(num_10c, "x 10c")
    if num_5c: print(num_5c, "x 5c")
    if num_1c: print(num_1c, "x 1c")
    
if __name__ == '__main__':
    # gets how much user must pay
    cost = eval (input ("Enter the cost (in cents):\n"))
    remaining = cost
    
    # runs until users has paid full cost
    while (remaining > 0):
        deposit = eval (input ("Deposit a coin or note (in cents):\n"))
        remaining -= deposit
    
    # user's change    
    if remaining:
        print ("Your change is:")    
        calc_change (abs(remaining))