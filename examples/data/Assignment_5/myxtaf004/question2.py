"""a vending machine simulator
Tafadzwa Moyo 
16 April 2014"""
#Takes in inputs
cost=int(input("Enter the cost (in cents):\n"))
if not cost:
    dep=0
else:
    dep=int(input("Deposit a coin or note (in cents):\n"))
#makes sure the deposit is hight than the cost
while cost>dep:
    dep+=int(input("Deposit a coin or note (in cents):\n"))
change=dep-cost
#initialising amount of dollars, 25c...
d1=0 
c25=0
c10=0
c5=0
c1=0

#Gets the amount dollarss, 25c,...
while change>=100:
    d1+=1
    change-=100
while change>=25:
    c25+=1
    change-=25
while change>=10:
    c10+=1
    change-=10
while change>=5:
    c5+=1
    change-=5
while change>=1:
    c1+=1
    change-=1
#displays the change
if dep-cost:
    print("Your change is:")
if d1!=0:
    print(d1, "x", "$1")
if c25!=0:
    print(c25, "x", "25c")
if c10!=0:
    print(c10, "x", "10c")
if c5!=0:
    print(c5, "x", "5c")
if c1!=0:
    print(c1, "x", "1c")