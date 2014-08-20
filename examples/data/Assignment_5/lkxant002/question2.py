#question 2

cost=eval(input("Enter the cost (in cents):\n"))
paid=0
while paid < cost:
    paid=paid+eval(input("Deposit a coin or note (in cents):\n"))

change=paid-cost
if change>0:
    print("Your change is:")

dol=0
c1=0
c5=0
c10=0
c25=0

dol=change//100
change=change-dol*100

c25=change//25
change=change-c25*25

c10=change//10
change=change-c10*10

c5=change//5
change=change-c5*5

c1=change

if dol>0:
    print(dol,"x $1")
if c25>0:
    print(c25,"x 25c")
if c10>0:
    print(c10,"x 10c")
if c5>0:
    print(c5,"x 5c")
if c1>0:
    print(c1,"x 1c")


