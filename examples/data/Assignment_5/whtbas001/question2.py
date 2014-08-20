
#def change_calc(x):
    #hundies = x//100
    #twofives = (x%100)//25
    #tenors = ((x%100)%25)//10
    #fivebop = (x%10)//5
    #units = x%5
    #changelist = [hundies, twofives, tenors, fivebop, units]
    #outputlist = ["x $1", "x 25c", "x 10c", "x 5c", "x 1c"]
    #print("Your change is:")
    #if x == 0:
        #print("0 x 1c")
    #for i in changelist:
        #if changelist[i] != 0:
            #print(changelist[i], outputlist[i])


def change_calc(x):
    hundies = x//100
#    print(hundies)
    twofives = (x%100)//25
#    print(twofives)
    tenors = ((x%100)%25)//10
#    print(tenors)
    fivebop = (((x%100)%25)%10)//5
#    print(fivebop)
    units = x%5
#    print(units)
    changelist = [hundies, twofives, tenors, fivebop, units]
    outputlist = ["x $1", "x 25c", "x 10c", "x 5c", "x 1c"]
    print("Your change is:")
    for i in range(len(outputlist)):
        if changelist[i] != 0:
            print(changelist[i], outputlist[i])


def vending_machine():
    cost = eval(input("Enter the cost (in cents):\n"))
    payment = 0
    while cost > payment:
        coin = eval(input("Deposit a coin or note (in cents):\n"))
        payment = payment + coin
    change_raw = payment - cost
    if change_raw != 0:
        change_calc(change_raw)

        
vending_machine()
        
        
        