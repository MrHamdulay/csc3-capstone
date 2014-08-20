# Dalise Steynfaard
# STYDAL001
# Assignment 5, question 2
# 12-04-2014

def vendingMachine():
    cost = eval(input('Enter the cost (in cents):\n'))
    change = 0
    payment = 0
    dollars = 0
    cents = 0
    
    while payment < cost:
        deposit = eval(input('Deposit a coin or note (in cents):\n'))
        payment += deposit
    change = payment - cost
    dollars = change // 100
    cents = change % 100
    
    if payment != cost:
        print('Your change is:')
        if dollars != 0:
            print(dollars,'x $1')
        if cents != 0:
            if cents >=25:
                change = cents // 25
                print(change,'x 25c')
                cents -= change*25
            if cents >= 10:
                change = cents // 10
                print(change,'x 10c')
                cents -= change*10
            if cents >= 5:
                change = cents // 5
                print(change,'x 5c')
                cents -= change*5
            if cents > 0:
                change = cents // 1
                print(change,'x 1c')
    
vendingMachine()