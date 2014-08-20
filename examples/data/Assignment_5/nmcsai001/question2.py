"""Saijil Nemchund
Question 2 
16 April 2014"""

cost=eval(input("Enter the cost (in cents):\n"))

amount=0

while amount<cost:
    new=eval(input("Deposit a coin or note (in cents):\n"))
    amount=amount+new

ch=amount-cost
change=ch

dollars=change//100
change=change-(dollars*100) #restating the value of change
quarters=(change)//25
change=change-(quarters*25)
ten_cents=(change)//10
change=change-(ten_cents*10)
five_cents=change//5
change=change-(five_cents*5)
one_cents=change

#Usage of if statements are necessary
if ch>0:
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