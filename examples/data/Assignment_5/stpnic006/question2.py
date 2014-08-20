#Nicholas Stephenson
#Vending Machine
#15 April 2014

import sys

paidthusfar=0


TotalCost = eval(input("Enter the cost (in cents):\n"))
#Total Cost, the cost provided
stillowing=TotalCost
while(paidthusfar < TotalCost):
    coininserted=eval(input("Deposit a coin or note (in cents):\n"))
    paidthusfar += coininserted
    stillowing -= coininserted

#Calculates the amount still owed, while cost is greater than owing


Return = -1*stillowing
#Converts Amount Owed (negative at this point) into change (positive)

if Return > 0:
    print("Your change is:")
    
    if ((Return//100)>0):
        print(round(Return//100), "x $1")
        Return -= Return//100*100
    
    if ((Return//25)>0):
        print(round(Return//25), "x 25c")
        Return -= Return//25*25
          
               
    if ((Return//10)>0):
            print(round(Return//10), "x 10c")
            Return -= Return//10*10
        
               
    if ((Return//5)>0):
            print(round(Return//5), "x 5c")
            Return -= Return//5*5


               
    if ((Return//1)>0):
            print(round(Return//1), "x 1c")
            Return -= Return//1*1
