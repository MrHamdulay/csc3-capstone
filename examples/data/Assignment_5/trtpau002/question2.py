"""Vending Machine simulator
Paul Truter
17 April 2014"""

#create function
def vendor():
    cost = eval(input("Enter the cost (in cents):\n"))
    payment = 0
    while payment < cost:
        payment += eval(input("Deposit a coin or note (in cents):\n"))
    if payment > cost:
        change = payment - cost
        if change != 0:
            print("Your change is:")
        dollar = change//100
        if dollar != 0:
            print(dollar,'x $1')
        twentyfive_cents = (change - dollar*100)//25
        if twentyfive_cents != 0:
            print(twentyfive_cents,'x 25c')
        ten_cents = (change - dollar*100 - twentyfive_cents*25)//10
        if ten_cents != 0:
            print(ten_cents,'x 10c')
        five_cents = (change - dollar*100 - twentyfive_cents*25 - ten_cents*10)//5
        if five_cents != 0:
            print(five_cents,'x 5c')
        one_cents = (change - dollar*100 - twentyfive_cents*25 - ten_cents*10 - five_cents*5)//1
        if one_cents != 0:
            print(one_cents,'x 1c')

vendor()