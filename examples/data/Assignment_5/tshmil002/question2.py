#Vending Machine  
#Mila Tshaka
#16 April 2014

cost = eval(input("Enter the cost (in cents):\n"))
if cost>0:
    payment = eval(input('Deposit a coin or note (in cents):\n'))

    #allows the user to enter more money untill cost is covered
    while (cost - payment) > 0:
        payment += eval(input('Deposit a coin or note (in cents):\n'))


    
    change = (payment-cost) #calculates the change (in cents)
    #calculates how much the change is composed of of dollars, 50,25,10 and 1 cents
    dollar = change//100
    cents = change - (100*dollar)
    twenty5 = cents//25
    cent = cents - (25*twenty5)
    ten = cent//10
    cen = cent - (10*ten)
    five = cen//5
    ce = cen - (5*five)

    #prints the change in its composed manner
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

