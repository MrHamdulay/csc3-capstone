"""Assigment 5 Question 2
Yaseen Sulliman
16 April 2014"""

cost=eval(input("Enter the cost (in cents):\n")) # cost of item in vending machine
if cost==0:
    ""
else:
    new_deposit=0
    while True:
        deposit=eval(input("Deposit a coin or note (in cents):\n")) #Amount inserted into vending mach9ine
        new_deposit+=deposit
        if new_deposit>=cost:
            break
    remain_deposit=new_deposit-cost
    if remain_deposit==0:
        ""
    else:
        print("Your change is:")
        dollar=remain_deposit//100
        twentyfive=(remain_deposit-(100*dollar))//25
        ten=(remain_deposit-(100*dollar)-(25*twentyfive))//10
        five=(remain_deposit-(100*dollar)-(25*twentyfive)-(10*ten))//5
        one=(remain_deposit-(100*dollar)-(25*twentyfive)-(10*ten)-(5*five))//1
        if dollar!=0:
            print(dollar,"x $1")
        if twentyfive!=0:
            print(twentyfive,"x 25c")
        if ten!=0:
            print(ten,"x 10c")
        if five!=0:
            print(five,"x 5c")
        if one!=0:
            print(one,"x 1c")
