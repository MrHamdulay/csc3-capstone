# Assignment 5 question 2
# Amy Brodie
# 16/04/2014

cost = eval(input("Enter the cost (in cents):\n"))
dollar = 0
cent25 = 0
cent10 = 0
cent5 = 0
cent1 = 0

# get user input for deposited amount and output the change
if cost != 0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    while (cost > deposit):
        deposit += eval(input("Deposit a coin or note (in cents):\n"))
        
    change = deposit - cost
    # check if there is change needed and how much    
    if change > 0:
        while  change:
            if change-100 >= 0:
                dollar += 1
                change -= 100
            elif change-25 >= 0:
                cent25 += 1
                change -= 25
            elif change-10 >= 0:
                cent10 += 1
                change -= 10
            elif change-5 >= 0:
                cent5 += 1
                change -= 5
            else:
                cent1 += 1
                change -= 1
    
        print("Your change is:")
        if dollar:
            print(dollar,"x $1")
        if cent25:
            print(cent25,"x 25c")
        if cent10:
            print(cent10,"x 10c")
        if cent5:
            print(cent5,"x 5c")
        if cent1:
            print(cent1,"x 1c")
        