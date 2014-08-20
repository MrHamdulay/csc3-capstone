#question3
#program to simulate a vending machine and calculate change based on the amount paid
# xola bilose
# 17/03/2014

# Promp input from the user and make sure that the cost is greater than 0
#question3
#program to simulate a vending machine and calculate change based on the amount paid



# Promp input from the user and make sure that the cost is greater than 0
dep=0
costs=eval(input("Enter the cost (in cents):\n"))
def pay(costs,dep):
    while costs!=0 and costs>0:
        cash=eval(input("Deposit a coin or note (in cents):\n"))
        dep=dep+cash
        nw=costs-cash
        cash=dep
        costs=nw
    return dep
# Change has been calculated and is being placed into its respective denominations

dep=pay(costs,dep)

# dep then becomes change to be given back, proceeding if statements then calculate change denominations according to their divisibility with number bearing similar decimal points

def change():   
    if dep-costs!=0 and dep-costs>0:
        print("Your change is:")
        change=dep-costs
        a=change//100
        a1=change%100
        if a>0:
            print(a,"x $1")
        b=a1//25
        b1=a1%25
        if b>0:
            print(b,"x 25c")
        c=b1//10
        c1=b1%10
        if c>0:
            print(c,"x 10c")
        d=c1//5
        d1=c1%5
        if d>0:
            print(d,"x 5c")
        e=d1//1
        if e>0:
            print(e,"x 1c")
change()