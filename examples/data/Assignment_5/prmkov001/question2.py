#Kovlin Perumal
import sys

cost = eval(input("Enter the cost (in cents):\n"))# Recieve cost variable

totPaid = 0
dummycost = cost

while(totPaid < cost): # Start while loop which runs while total Paid < cost
    coin = eval(input("Deposit a coin or note (in cents):\n"))
    totPaid += coin
    dummycost -= coin
    
change = (-1 * dummycost) #Store change in variable

if change > 0 :

    print("Your change is:")

    #Account for different coins to be dispensed
    if ((change//100)>0) :
        print(round(change//100),'x $1')
    
        change-= change//100 * 100

    if ((change//25)>0) :
        print(round(change//25),'x 25c')
    
        change-= change//25 * 25

    if ((change//10)>0) :
        print(round(change//10),'x 10c')
    
        change-= change//10 * 10

    if ((change//5)>0) :
        print(round(change//5),'x 5c')
    
        change-= change//5 * 5


    if ((change//1)>0) :
        print(round(change//1),'x 1c')
    
        change-= change//1 * 1

