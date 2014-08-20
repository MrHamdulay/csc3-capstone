"""A program that simulates a vending machine
Jason Findlay
15/04/2014"""

amount=eval(input("Enter the cost (in cents):\n"))
paid=0

#Loop till enough money has been paid
while paid<amount:
    paid+=eval(input("Deposit a coin or note (in cents):\n"))
    
#Calculate change
change=paid-amount

#Check change is needed
if change!=0:
    print("Your change is:")

#Print out change
if change//100>0:
    print(change//100, "x $1")
    change%=100
if change//25>0:
    print(change//25, "x 25c")
    change%=25
if change//10>0:
    print(change//10, "x 10c")
    change%=10
if change//5>0:
    print(change//5, "x 5c")
    change%=5
if change//1>0:
    print(change//1, "x 1c")
