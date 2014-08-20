""" Vending machine program
tayla george
17 april 2014"""

def change():
    cost = eval(input("Enter the cost (in cents):" '\n'))
    deposit = 0
    while deposit<cost:
        amount_deposit = eval(input("Deposit a coin or note (in cents):" '\n'))
        deposit+=amount_deposit
    change=deposit-cost
    new_change=change

    if change != 0:
        print("Your change is:")
    if change >= 100:
        print(change//100, "x $1")
        new_change = change%100
    if new_change >= 25:
        print(new_change//25, "x 25c")
        new_change = new_change%25

    if new_change >= 10:
        print(new_change//10,"x 10c")
        new_change = new_change%10            
        
    if new_change >= 5:
        print(new_change//5, "x 5c")
        new_change = new_change%5
     
    if new_change != 0:
        print(new_change//1, "x 1c")
            
change()