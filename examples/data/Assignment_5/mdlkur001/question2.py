#14/04/14
#Kureshlen Moodley
#MDLKUR001

cost=eval(input("Enter the cost (in cents):\n"))
amount=0
if cost>0:   
    amount=eval(input("Deposit a coin or note (in cents):\n"))

while amount<cost:   
    new=eval(input("Deposit a coin or note (in cents):\n"))
    amount=amount+new
#repeats until enough change is eneterd
change=amount-cost
check=change

dollars=change//100
change=change-(dollars*100)
quarters=(change)//25
change=change-(quarters*25)
ten_cents=(change)//10
change=change-(ten_cents*10)
five_cents=change//5
change=change-(five_cents*5)
one_cents=change

#calculates change to be given
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
# Determines amount of each unit of change