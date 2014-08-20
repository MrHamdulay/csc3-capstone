import math
global payed
global cost

def findChange(value):
    if value == 0 :
        print(end = "")
    else:
        print("Your change is:")
    
    if value//100 > 0:
        print(int(value//100) , "x $1")
        value -= value//100 * 100
    
    if value//25 > 0:
        print(int(value//25) , "x 25c")
        value -= value//25 * 25        

    if value//10 > 0:
        print(int(value//10) , "x 10c")
        value -= value//10 * 10
        
    if value//5 > 0:
        print(int(value//5) , "x 5c")
        value -= value//5 * 5
        
    if value//1 > 0:
        print(int(value//1), "x 1c")
        value -= value//1 * 1     

def posOrNeg(value):
    if value < 0:
        requestMoney()
    else:
        findChange(value)

def requestMoney():
    value = eval(input("Deposit a coin or note (in cents):\n"))
    global payed
    payed += value
    global cost
    posOrNeg(calcDiff(payed, cost))

def calcDiff(val1, val2):
    return val1 - val2


        
cost = eval(input("Enter the cost (in cents):\n"))
if cost > 0:
    payed = eval(input("Deposit a coin or note (in cents):\n"))
    posOrNeg(calcDiff(payed,cost))