def vendingmachine():
    #This gets and assesses an input from the user
    x = eval(input("Enter the cost (in cents):\n"))
    money = 0
    while money<x:
        y = eval (input("Deposit a coin or note (in cents):\n"))
        money = money + y 
    #This line calculates change 
    change = money - x
    # this organises the different coins that can be given and assigns values to them 
    a, b, c, d, e = 100, 25, 10, 5, 1
    # this line acts as a counter to keep score of how many of each coin is being used for the change 
    acount, bcount, ccount, dcount, ecount = 0, 0, 0, 0, 0
    # this line gives a picture representation of the different coins to be returned
    apic = "$1"
    bpic = "25c"
    cpic = "10c"
    dpic = "5c"
    epic = "1c"
    # This line is responsible for sorting the change
    while change>=100:
        change = change - a
        acount = acount + 1
    while change>=25:
        change = change - b
        bcount = bcount + 1
    while change>=10:
        change = change - c
        ccount = ccount + 1
    while change>=5:
        change = change - d
        dcount = dcount + 1 
    while change>=1:
        change = change - e
        ecount = ecount + 1
    # This final line gives the change to the user
    if acount==0 and bcount==0 and ccount==0 and dcount==0 and ecount==0:
        s=2
    else:
        print ("Your change is:")
        if acount!=0:        
            print (acount, "x", apic)
        if bcount!=0:
            print (bcount, "x", bpic)
        if ccount!=0:
            print (ccount, "x", cpic)
        if dcount!=0:
            print (dcount, "x", dpic)
        if ecount!=0:
            print (ecount, "x", epic)

vendingmachine()