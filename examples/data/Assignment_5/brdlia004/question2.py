"""Vending Machine"""
#Liam Brodie
#12 April 2014
#BRDLIA004
#Assignment 5

cost = eval(input("Enter the cost (in cents):\n"))

if cost > 0:
    payment = 0
    while payment <= cost:
        payment += eval(input("Deposit a coin or note (in cents):\n"))
        if payment == cost:
            break
        
if cost > 0:    
    change = payment - cost
    if len(str(change)) >= 3:
        if len(str(change)) == 3:
            DolChange = str(change)[0]
        elif len(str(change)) >= 3:
            DolChange = str(round(change, -2)//100)
    else:
        DolChange = 0
    QuartChange = str((change - int(DolChange)*100)//25)
    TenChange   = str((change - int(DolChange)*100 - int(QuartChange)*25)//10)
    FiveChange  = str((change - int(DolChange)*100 - int(QuartChange)*25 - int(TenChange)*10)//5)
    OneChange   = str((change - int(DolChange)*100 - int(QuartChange)*25 - int(TenChange)*10 - int(FiveChange)*5)//1)


def CHANGE():
    """Calculates Change"""
    print("Your change is:")
    if int(DolChange) > 0:
        print(DolChange+" x $1")
    if int(QuartChange) > 0:
        print(QuartChange+" x 25c")
    if int(TenChange) > 0:
        print(TenChange+" x 10c")
    if int(FiveChange) > 0:
        print(FiveChange+" x 5c")
    if int(OneChange) > 0:
        print(OneChange+" x 1c")

if cost > 0:        
    if change > 0:        
        CHANGE()
        