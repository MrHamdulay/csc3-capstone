# Question 2 - Assignment 5
# Vending machine
# Written by: Laene van Niekerk

amount = eval(input("Enter the cost (in cents):\n"))
if amount != 0:
    paid = eval(input("Deposit a coin or note (in cents):\n"))
    while paid < amount:
        more_paid = eval(input("Deposit a coin or note (in cents):\n"))     # Prompts user to enter more money if amount too little
        paid = paid + more_paid
        if paid >= amount:
            break       # Stops while loop once the money entered is equal to or more than the amount required
    
    dollar = 0
    twenty_five = 0
    ten = 0
    five = 0
    one = 0

    change = paid - amount

    while change > 0:
        if change >= 100:
            dollar = dollar + (change//100)
            change = change - (dollar * 100)
        elif 100 > change >= 25:
            twenty_five = twenty_five + (change//25)
            change = change - (twenty_five * 25)
        elif 25 > change >= 10:
            ten = ten + (change//10)
            change = change - (ten * 10)
        elif 10 > change >= 5:
            five = five + (change//5)
            change = change - (five * 5)
        elif 5 > change >= 1:
            one = one + (change // 1)
            change = change - (one * 1)        

    if paid != amount:
        print("Your change is:")
        if dollar > 0:
            print(dollar, "x $1")
        if twenty_five > 0:
            print(twenty_five, "x 25c")
        if ten > 0:
            print(ten, "x 10c")
        if five > 0:
            print(five, "x 5c")
        if one > 0:
            print(one, "x 1c")