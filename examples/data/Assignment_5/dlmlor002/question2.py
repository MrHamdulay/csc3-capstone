"""program to show user amount of change received after giving deposit(s)
Lorena Dal Maso
16 April 2014"""

cost=eval(input("Enter the cost (in cents):\n"))
if cost==0:
    print()
    
if cost>0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
while cost>deposit:
    deposit=deposit + eval(input("Deposit a coin or note (in cents):\n"))
    change=deposit-cost
    dol=change//100 
    quart=change%100//25 
    ten_cent=change%100%25//10
    five_cent=change%100%25%10//5
    one_cent=change%100%25%10%5//1

change=deposit-cost    
dol=change//100 
quart=change%100//25 
ten_cent=change%100%25//10
five_cent=change%100%25%10//5
one_cent=change%100%25%10%5//1    
        
if cost<deposit:
    print("Your change is:")
    if dol>0:
        print(dol," x $1",sep="")
    if quart>0:
        print(quart," x 25c",sep="")
    if ten_cent>0:
        print(ten_cent," x 10c",sep="")
    if five_cent>0:
        print(five_cent," x 5c",sep="")
    if one_cent>0:
        print(one_cent," x 1c",sep="")

    
    
    
    
    
    
    