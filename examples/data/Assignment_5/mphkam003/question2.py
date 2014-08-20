"""program simulates a vending machine
kamogelo mphela
15 april 2014"""
def vendor():
    cost = eval(input("Enter the cost (in cents):\n"))
    # runs only if there is a cost
    if cost != 0:
    
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        if deposit < cost:
            while deposit < cost:
                deposit+= eval(input("Deposit a coin or note (in cents):\n"))
                change = deposit - cost
                dollar = change//100
                quater = (change - dollar*100)//25
                ten_cents = ((change-dollar*100)-quater*25)//10
                five_cents = (((change-dollar*100)-quater*25)-ten_cents*10)//5
                one_cents = ((((change-dollar*100)-quater*25)-ten_cents*10)-five_cents*5)
            if change:
                print("Your change is:")
            if dollar:
                print(dollar, "x $1")
            if quater:
                print(quater, "x 25c")
            if ten_cents:
                print(ten_cents, "x 10c")
            if five_cents:
                print(five_cents, "x 5c")
            if one_cents:
                print(one_cents, "x 1c")
                    
        else:
            change = deposit - cost
            dollar = change//100
            quater = (change - dollar*100)//25
            ten_cents = ((change-dollar*100)-quater*25)//10
            five_cents = (((change-dollar*100)-quater*25)-ten_cents*10)//5
            one_cents = ((((change-dollar*100)-quater*25)-ten_cents*10)-five_cents*5)
                
                
            if change:
                print("Your change is:")
            if dollar:
                print(dollar, "x $1")
            if quater:
                print(quater, "x 25c")
            if ten_cents:
                print(ten_cents, "x 10c")
            if five_cents:
                print(five_cents, "x 5c")
            if one_cents:
                print(one_cents, "x 1c")
vendor()