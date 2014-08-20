"""VENDING MACHINE
APHIWE BALENI
4/15/2014"""

cost=eval(input('Enter the cost (in cents):\n'))
change=0
if cost!=0:
    y = eval(input('Deposit a coin or note (in cents):\n'))
    while y<cost:
        y+=eval(input('Deposit a coin or note (in cents):\n'))
    change=y-cost
    dollars=change//100
    quarters=(change-(dollars*100))//25
    pennys=(change-dollars*100-25*(quarters))//10
    fivecent=((change-dollars*100-25*(quarters))-pennys*10)//5
    cents=int(((change-dollars*100-25*(quarters))-fivecent*5-pennys*10)//5)
    dollars=int(dollars)
    quarters=int(quarters)
    pennys=int(pennys)
    fivecent=int(fivecent)
#print(dollars,quarters,pennys,fivecent,cents,sep='+')
if change!=0:
    print('Your change is:')
    if dollars!=0:
        print(dollars,'x','$1')
    if quarters!=0:
        print(quarters,'x','25c')
    if pennys!=0:
        print(pennys,'x','10c')
    if fivecent!=0:
        print(fivecent,'x','5c')
    if cents!=0:
        print(cents,'x','1c')