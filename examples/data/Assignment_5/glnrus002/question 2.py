#question 2
#glnrus002
cost=eval(input("Enter the cost(in cents):\n"))
total=0
work=0
while total<cost:
    work=eval(input("Deposit a coin or note (in cents):\n"))
    total=total+work
    
change=total-cost

if change>0:
    dollars=change//100
    change=change%100
    quarters=change//25
    change=change%25
    ten=change//10
    change=change%10
    five=change//5
    change=change%5
    cent=change
    print("Your change is:")
    
    if dollars>0:
        print(dollars,"x $1")
    if quarters>0:
        print(quarters,"x 25c")
    if ten>0:
        print(ten,"x 10c")
    if five>0:
        print(five,"x 5c")
    if change>0:
        print(change, "x 1c")