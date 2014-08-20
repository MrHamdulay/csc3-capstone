"""vending machine
Lauren Denny
15 April 2014"""

paid = 0

#ask for a cost in cents
cost = eval(input("Enter the cost (in cents):\n"))

#asks for a deposit until the cost is covered
while paid<cost:
    paid = paid + eval(input("Deposit a coin or note (in cents):\n"))

#total change in cents
change = paid-cost

if change!=0:
    #lists with corresponding denomination names and denomination values in cents
    denom = ["$1","25c","10c","5c","1c"]
    value = [100,25,10,5,1]
    #displays total change as (number of coin) x denomination of coin for each denomination
    print("Your change is:")
    for i in range (5):
        c = change//value[i]
        change = change - c*value[i]
        if c!=0:
            print(c,"x",denom[i])

