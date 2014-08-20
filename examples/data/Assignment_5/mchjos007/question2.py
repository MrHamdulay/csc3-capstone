amountdeposited = 0
cost = eval(input("Enter the cost (in cents):\n"))
while cost > amountdeposited:
    amountdeposited += eval(input("Deposit a coin or note (in cents):\n"))
change = amountdeposited - cost
if change != 0:
    print("Your change is:")
if change >= 100:
    numofhunds = 0
    while change >= 100:
        change -= 100
        numofhunds += 1
    print (numofhunds, "x $1")
if change >= 25:
    numof25s = 0
    while change >= 25:
        change -= 25
        numof25s += 1
    print (numof25s, "x 25c")
if change >= 10:
    numof10s = 0
    while change >= 10:
        change -= 10
        numof10s += 1
    print (numof10s, "x 10c")
if change >= 5:
    numof5s = 0
    while change >= 5:
        change -= 5
        numof5s += 1
    print (numof5s, "x 5c")
if change >= 1:
    numof1s = 0
    while change >= 1:
        change -= 1
        numof1s += 1
    print (numof1s, "x 1c")
    
