cost=eval(input("Enter the cost (in cents):\n"))

total=0

while total<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    total+=deposit
    
change=total-cost
t=change
ones = change//100
change=change-ones*100

quarters=change//25
change=change-quarters*25

dimes=change//10
change=change-dimes*10

nickels=change//5
change=change-nickels*5

pennies=change
if t:
    print("Your change is:")
    if ones>0:
        print(ones, "x $1")
    if quarters>0:
        print(quarters, "x 25c")
    if dimes>0:
        print(dimes, "x 10c")
    if nickels>0:
        print(nickels, "x 5c")
    if pennies>0:
        print(pennies, "x 1c")