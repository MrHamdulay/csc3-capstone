#TEVIN CHETTY
#15 APRIL 2014
#QUESTION 2

cost=eval(input("Enter the cost (in cents):\n"))
amount=0
if cost>0:   
    amount=eval(input("Deposit a coin or note (in cents):\n"))

while amount<cost:    #stops asking for money once you have put in enough
    new=eval(input("Deposit a coin or note (in cents):\n"))
    amount=amount+new

change=amount-cost
check=change

dollars=change//100
change=change-(dollars*100)#redefine change to take into account amount of each denomination given back
quarters=(change)//25
change=change-(quarters*25)
ten_cents=(change)//10
change=change-(ten_cents*10)
five_cents=change//5
change=change-(five_cents*5)
one_cents=change

#have to use if statements as otherwise it would print 0 x the value
if check>0:
    print("Your change is:")
    if dollars>0:
        print(dollars, "x $1")
    if quarters>0:
        print(quarters, "x 25c")
    if ten_cents>0:
        print(ten_cents, "x 10c")
    if five_cents>0:
        print(five_cents, "x 5c")
    if one_cents>0:
        print(one_cents, "x 1c")
