"""Create vending-type machine to dispense change
Ross Eyre
16/04/2014"""

import sys

#get user input for cost and deposit
cost = eval(input("Enter the cost (in cents):\n"))

if(cost==0):
    sys.exit()
dep = eval(input("Deposit a coin or note (in cents):\n"))
while cost > dep:
    dep += eval(input("Deposit a coin or note (in cents):\n"))

#calculate change
changeC = dep - cost

if(changeC != 0):
    #if there is change
    #determine which divisions of money to dispense depending on ammount of change
    oneDol =  changeC//100
    rem = changeC%100
    twenFiveC = rem//25
    rem = rem%25
    tenC = rem//10
    rem = rem%10
    fiveC = rem//5
    
    #display change in coins if there is change
    print("Your change is:")
    if(oneDol != 0):
        print(oneDol, "x", "$1")
    if(twenFiveC != 0):
        print(twenFiveC , "x", "25c")
    if(tenC != 0):
        print(tenC, "x","10c")
    if(fiveC != 0):
        print(fiveC, "x", "5c")