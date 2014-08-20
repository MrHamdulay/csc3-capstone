# calculates change given by a vending machine
# Edwin Samuels
# Student number Smledw002
# 16 april 2014


cost = eval(input("Enter the cost (in cents):\n"))
deposit  = 0

while deposit < cost: #request a deposit till the cost is met
    deposit += eval(input("Deposit a coin or note (in cents):\n"))
    
dollars = 0
quarts = 0
tens = 0
fives = 0

cost = deposit - cost  #calculates the new change re-using the cost variable
if deposit - cost != deposit:  #checks if theres change due
    if cost//100 > 0:
        dollars = cost//100
        cost %= 100

    if cost//25 > 0:
        quarts = cost//25
        cost %= 25

    if cost//10 > 0:
        tens = cost//10
        cost %= 10

    if cost//5 > 0:
        fives = cost//5
        cost %= 5

    print("Your change is:")

    if dollars > 0:
        print(dollars,"x $1")

    if quarts > 0:
        print(quarts, "x 25c")

    if tens > 0:
        print(tens, "x 10c")

    if fives > 0:
        print(fives, "x 5c")
    if cost > 0:
        print(cost, "x 1c")


