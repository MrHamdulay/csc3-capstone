#program used to simulate a vending machine using specific cent values
#nkosi gumede
#16/04/2014

#create all necessary variables
#coins are only 1c, 5c, 10c, 25c and $1
deposit=0
change=0
cost=eval(input("Enter the cost (in cents):\n"))
while cost>deposit:
    coin=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+coin
change=deposit-cost
#to convert change amt into dollars and cents:
#for number of 100cents
a=change//100
change=change-(a*100) #keep calculating remaining change after biggest coin distributed
#for number of 25cents
b=change//25
change=change-(b*25)
#for number of 10cents
c=change//10
change=change-(c*10)
#for number of 5cents
d=change//5
change=change-(d*5)
#for number of 1cents
e=change//1
change=change-(e*1)
#now for the output of change
if deposit-cost>0:
    print("Your change is:")
if a>0:
    print(a,"x $1")
if b>0:
    print(b,"x 25c")
if c>0:
    print(c,"x 10c")
if d>0:
    print(d,"x 5c")
if e>0:
    print(e,"x 1c")