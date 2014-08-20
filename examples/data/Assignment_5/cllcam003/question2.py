# vending machine program 
# CLLCAM003
# 15/04/2014

cost= eval(input("Enter the cost (in cents):\n"))
if cost>0:
    dep_1=0
    while dep_1<=cost: # if money gives is less than or equal to items cost
        dep_2=eval(input("Deposit a coin or note (in cents):\n"))
        dep_1+=dep_2
        if dep_1-cost>=0:
            break
    change=dep_1-cost #amount paid subtracted from amount owed

    if change>0:
        print("Your change is:")
    if change//100!=0:
        print(change//100, "x $1")
        change=change-(100*(change//100))

    if change//25!=0:
        print(change//25, "x 25c")
        change=change-(25*(change//25))

    if change//10!=0:
        print(change//10, "x 10c")
        change=change-(10*(change//10))

    if change//5!=0:
        print(change//5, "x 5c")
        change=change-(10*(change//5))    

    if change<0:
        print(change, "x 1c")