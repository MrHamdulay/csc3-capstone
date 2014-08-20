'''Vending machine
Mokoena Mafologele
16/04/2014'''

cost = int(input("Enter the cost (in cents):\n"))
if cost>0:
    deposit = int(input('Deposit a coin or note (in cents):\n'))

    #ask user to put in more until cost is reached or exceeded
    while (cost - deposit) > 0:
        deposit += int(input('Deposit a coin or note (in cents):\n'))


    
    change = (deposit-cost) #calculates change
    #compose into coins
    d = change//100
    cents = change - (100*d)
    twenty5 = cents//25
    cent = cents - (25*twenty5)
    ten = cent//10
    cen = cent - (10*ten)
    five = cen//5
    ce = cen - (5*five)

    #prints your change into its parts
    if change!=0:
        print("Your change is:")
        if d != 0:
            print(d,'x $1')
        if twenty5 != 0:    
            print(twenty5,'x 25c')
        if ten != 0:
            print(ten,'x 10c')
        if five != 0:
            print(five,'x 5c')
        if ce != 0:
            print(ce,'x 1c')

