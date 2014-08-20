'''vending machine
Tim Mostert
16 04 2014'''

cost = eval(input("Enter the cost (in cents):\n"))
total_deposited = 0
while total_deposited < cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    total_deposited += deposit
change = total_deposited - cost
def vendingmachine():
    change = total_deposited - cost
    if change == 0:
        return
    else:
        no_dollar = change//100
        change = change % 100
        no_25c = change//25
        change = change % 25
        no_10c = change//10
        change = change % 10
        no_5c = change//5
        change = change % 5
        no_1c = change//1
        print("Your change is:")
        if no_dollar > 0:
            print(no_dollar,"x $1")
        if no_25c > 0:
            print(no_25c,"x 25c")
        if no_10c > 0:
            print(no_10c,"x 10c")
        if no_5c > 0:
            print(no_5c,"x 5c")
        if no_1c > 0:
            print(no_1c,"x 1c")

vendingmachine()            

    
