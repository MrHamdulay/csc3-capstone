"""Program to Simulate a Vending Machine
16 April 2014
Sithasibanzi Kondleka"""

cost = eval(input("Enter the cost (in cents):\n"))
deposit = 0
while deposit < cost:
    deposit1 = eval(input("Deposit a coin or note (in cents):\n"))
    deposit+=deposit1
change = deposit-cost
if change > 0:
    print("Your change is:")
    dollar = change//100
    change = change-(dollar*100)
    quarter = change//25
    change = change-(quarter*25)
    tenCents = change//10
    change = change-(tenCents*10)
    fiveCents = change//5
    change = change-(fiveCents*5)
    oneCents = change//1
    change = change-(oneCents*1)
    if dollar!=0:
        print(dollar,"x $1")
    if quarter!=0:
        print(quarter,"x 25c")
    if tenCents!=0:
        print(tenCents,"x 10c")
    if fiveCents!=0:
        print(fiveCents,"x 5c")
    if oneCents!=0:
        print(oneCents,"x 1c")