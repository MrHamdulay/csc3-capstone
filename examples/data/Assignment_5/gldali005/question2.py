# program to simulate a vending machine and calculate change based on the amount paid
# Ali Goldstein
# 16 April 2014

#prompt the user to enter a cost
cost = eval(input("Enter the cost (in cents):\n"))

#creating variables
tot=0
oneDollar = 0
twentyFive = 0
ten = 0
five = 0
one = 0

#prompting the user to enter deposit amounts until the deposit exceeds or meets the cost amount
while cost>tot:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    tot =tot+ deposit

difference = tot-cost

while ((difference/100)>=1):
    oneDollar +=1
    difference -= 100

while ((difference/25)>=1):
    twentyFive +=1
    difference -= 25

while ((difference/10)>=1):
    ten +=1
    difference -= 10

while ((difference/5)>=1):
    five +=1
    difference -= 5

while ((difference/1)>=1):
    one +=1
    difference -= 1

#only prints this if the deposit they entered is greater than the cost.
#prints the different amounts of change in the different denominations.
if tot>cost:    
    print("Your change is:")
    if (oneDollar > 0):
        print(str(oneDollar)+" x $1")
    if (twentyFive > 0):
        print(str(twentyFive)+" x 25c")
    if (ten > 0):
        print(str(ten)+" x 10c")
    if (five > 0):
        print(str(five)+" x 5c")
    if (one > 0):
        print(str(one)+" x 1c")