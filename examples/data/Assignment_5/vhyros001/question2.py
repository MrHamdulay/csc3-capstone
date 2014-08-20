"""Assignment 5 question 2 Vending machine simulator
Ross van der Heyde VHYROS001
13 April 2014"""

cost = eval(input("Enter the cost (in cents):\n"))
paid = 0

while paid < cost :
    paid += eval(input("Deposit a coin or note (in cents):\n"))


if paid > cost :
    #Assume that all change is given in coins only and coins come in the following
    #denominations: 1c, 5c, 10c, 25c, $1
    #penny, nickel, dime, quarter, dollar 
    print("Your change is:")
    change = paid - cost
    
    doll = change // 100
    change -= doll*100
    
    q = change // 25
    change -= q * 25
    
    d = change // 10
    change -= 10* d

    n = change // 5
    change -= n* 5
    
    p = change
    
    if doll >0:
        print(doll, "x $1")
    if q >0:
        print(q, "x 25c")    
    if d >0:
        print(d, "x 10c")
    if n >0:
        print(n, "x 5c")                        
    if p >0:
        print(p, "x 1c")