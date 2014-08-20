'''Question 2 of Assignment 5 of CSC1015F
A vending machine simulation
Author: Reid Swan
2014-04-14'''

def VendingMachine():
    """Simulates a vending machine"""
    cost = eval(input("Enter the cost (in cents):\n"))
    if cost == 0:
        return
    deposit_str = ""
    try:
        deposit_str = input("Deposit a coin or note (in cents):\n")
    except EOFError:
        pass
    deposit = 0
    if deposit_str.isdigit():
        deposit = eval(deposit_str)
    while deposit < cost:
        try:
            deposit_str = input("Deposit a coin or note (in cents):\n")
        except EOFError:
            pass
        else:
            if deposit_str.isdigit():
                deposit += eval(deposit_str)
    remainder = deposit - cost
    # the following variables count the output of coins
    dollars = 0
    cent25 = 0
    cent10 = 0
    cent5 = 0
    cent1 = 0
    if remainder != 0: print("Your change is:")
    while remainder >= 100: # count of 100 cents = $1
        remainder -= 100
        dollars += 1
    if dollars > 0:
        print(dollars, "x $1")
    while remainder >= 25: # count of 25 cent coins
        remainder -= 25
        cent25 += 1
    if cent25 > 0:
        print(cent25, "x 25c")
    while remainder >= 10:
        remainder -= 10
        cent10 += 1
    if cent10 > 0:
        print(cent10, "x 10c")
    while remainder >= 5:
        remainder -= 5
        cent5 += 5
    if cent5 > 0:
        print(cent5, "x 5c")
    if remainder > 0:
        print(remainder, "x 1c")
        
if __name__ == "__main__":
    VendingMachine()