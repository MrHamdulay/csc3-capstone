'''Assignment 5 question 2 Vending machine
Adam Smith
16 April 2014'''

cost = eval(input("Enter the cost (in cents):\n"))

#Define variables
TotalPaid = 0
amountPaid = 0
OneDollar = 0
TwentyFiveC = 0
TenC = 0
FiveC = 0
OneC = 0

while cost > TotalPaid: #run until cost has been exceded
    amountPaid = eval(input("Deposit a coin or note (in cents):\n"))
    TotalPaid = TotalPaid + amountPaid
    
change = TotalPaid - cost

if change !=0:
    print("Your change is:")

while change != 0: #spilt the change into the allowed amounts
    if change >= 100:
        change = change - 100
        OneDollar +=1
    elif change >= 25:
        change = change - 25
        TwentyFiveC +=1
    elif change >= 10:
        change = change - 10
        TenC +=1
    elif change >= 5:
        change = change - 5
        FiveC +=1
    elif change >= 1:
        change = change - 1
        OneC +=1
       
#return the change in the amounts specified
if OneDollar > 0:
    print(OneDollar, "x $1")
if TwentyFiveC > 0:
    print(TwentyFiveC, "x 25c")
if TenC > 0:
    print(TenC, "x 10c")
if FiveC > 0:
    print(FiveC, "x 5c")
if OneC > 0:
    print(OneC, "x 1c")