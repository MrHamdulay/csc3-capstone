"""Aiden Walton
WLTAID001
Question 2 - vending machine calculator"""

cost=eval(input("Enter the cost (in cents):\n"))
totdeposit=0
while totdeposit<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    totdeposit+=deposit
change=totdeposit-cost
dollar=change//100
incr1=(change-(dollar*100))//25
incr2=(change-(dollar*100)-(incr1*25))//10
incr3=(change-(dollar*100)-(incr1*25)-(incr2*10))//5
incr4=(change-(dollar*100)-(incr1*25)-(incr2*10)-(incr3*5))
if totdeposit!=cost:
    print("Your change is:")
    if dollar>0:
        print(dollar,"x $1")
    if incr1 >0:
        print(incr1,"x 25c")
    if incr2>0:
        print(incr2,"x 10c")
    if incr3>0:
        print(incr3,"x 5c")
    if incr4>0:
        print(incr4,"x 1c")