#vending machine program
#omphemetse molusi
#17 april 2014

#the beginning of the program with the cost and deposit amounts
cost = eval(input("Enter the cost (in cents):\n"))
if cost>0:
    deposit = eval(input('Deposit a coin or note (in cents):\n'))

    while (cost - deposit) > 0:
        deposit += eval(input('Deposit a coin or note (in cents):\n'))


    #change calculation
    change = (cost-payment)*-1
    dollar = change//100
    cents = change - (100*dollar)
    twenty5 = cents//25
    cent = cents - (25*twenty5)
    ten = cent//10
    cen = cent - (10*ten)
    five = cen//5
    ce = cen - (5*five)

    #the change outcome
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

