cost=eval(input("Enter the cost (in cents):\n"))
mp=0
while True:
    if mp < cost:
        dep=eval(input("Deposit a coin or note (in cents):\n"))
        mp+=dep
    elif mp == cost:
        
        break
    elif mp >cost:
        change= mp - cost
        
        dol = change //100
        quart = (change-100*dol) // 25
        dime = (change - 100*dol - 25*quart) // 10
        nickel = (change -100 *dol - 25*quart - 10 * dime) //5
        penny = change -100 *dol - 25*quart - 10 * dime - nickel *5
        print("Your change is:")
        if dol != 0:
            print(dol, "x $1")
        if quart !=0:
            print(quart, "x 25c")
        if dime !=0:
            print(dime, "x 10c")
        if nickel !=0:
            print(nickel, "x 5c")
        if penny !=0:
            print(penny, "x 1c")
        break