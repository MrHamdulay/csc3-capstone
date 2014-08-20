"""Vending Machine
Yamkela Venfolo
10 April 2014"""

cost = eval(input("Enter the cost (in cents):\n"))
if cost>0:
    payment = eval(input('Deposit a coin or note (in cents):\n'))

    #Checks if the amount enterd by the user is enough
    while (cost - payment) > 0:
        payment += eval(input('Deposit a coin or note (in cents):\n'))


    #calculates the change of the user and determines how many dollars, 25 cents, 10 cents and cents in the change
    change = (cost-payment)*-1
    dollar = change//100
    cents = change - (100*dollar)
    twenty5 = cents//25
    cent = cents - (25*twenty5)
    ten = cent//10
    cen = cent - (10*ten)
    five = cen//5
    ce = cen - (5*five)

    #prints the change
    if change!=0:
        print("Your change is:")
        if dollar != 0:
            print(dollar,'x $1')
        if twenty5 != 0:    
            print(twenty5,'x 25c')
        if ten != 0:
            print(ten,'x 10c')
        if five != 0:
            print(five,'x 5c')
        if ce != 0:
            print(ce,'x 1c')

