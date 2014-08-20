total = eval(input("Enter the cost (in cents):\n"))
paid = 0
while paid < total:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    paid += deposit
totalChange = paid - total
ones, fives, tens, twentyFives, hundreds = 0, 0, 0, 0, 0
if totalChange != 0:
    while totalChange >= 100:
        hundreds += 1
        totalChange -= 100
    while totalChange >= 25:
        twentyFives += 1
        totalChange -= 25
    while totalChange >= 10:
        tens += 1
        totalChange -= 10
    while totalChange >= 5:
        fives += 1
        totalChange -= 5
    while totalChange >= 1:
        ones += 1
        totalChange -= 1  
    print("Your change is:")
    if hundreds != 0:
        print(hundreds, "x $1")
    if twentyFives != 0:
        print(twentyFives, "x 25c")    
    if tens != 0:
        print(tens, "x 10c")
    if fives != 0:
        print(fives, "x 5c")   
    if ones != 0:
        print(ones, "x 1c")  