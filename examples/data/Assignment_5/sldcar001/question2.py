def vendingmath(x):
    dol=x//100
    dx=x-dol*100
    quart=dx//25
    qx=dx-quart*25
    ten=qx//10
    tx=qx-ten*10
    fiv=tx//5
    fx=tx-fiv*5
    ox=fx
    if dol>0:
        print(dol,"x $1")
    if quart>0:
        print(quart,"x 25c")
    if ten>0:
        print(ten,"x 10c")
    if fiv>0:
        print(fiv,"x 5c")
    if ox>0:
        print(ox,"x 1c")

def vendingmachine():
    cost=eval(input("Enter the cost (in cents):\n"))
    if cost>0:
        pay=eval(input("Deposit a coin or note (in cents):\n"))
        while pay<cost:
            payagain=eval(input("Deposit a coin or note (in cents):\n"))
            pay=pay+payagain
        x=pay-cost
        if x>0:
            print("Your change is:")
        vendingmath(x)
vendingmachine()