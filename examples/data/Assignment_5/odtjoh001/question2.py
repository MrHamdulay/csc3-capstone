cost = eval(input("Enter the cost (in cents):\n"))
if cost > 0:
    dep = eval(input("Deposit a coin or note (in cents):\n"))

    while dep < cost:
        dep += eval(input("Deposit a coin or note (in cents):\n"))
    
    change  = dep - cost
    if change > 0:
        dollars = change // 100
        change = change - (dollars *100)
        twentyfive = change // 25
        change = change - (twentyfive *25)
        ten = change // 10
        change = change - (ten *10)
        five = change // 5
        change = change - (five *5)
        one = change // 1
        print("Your change is:")
        if dollars != 0:
            print(dollars, "x $1")
        if twentyfive != 0:
            print(twentyfive, "x 25c")
        if ten != 0:
            print(ten, "x 10c")
        if five != 0:
            print(five, "x 5c")
        if one != 0:
            print(one, "x 1c")