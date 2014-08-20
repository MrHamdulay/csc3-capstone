def change_calc():
    #ask for money
    total = eval(input("Enter the cost (in cents):\n"))
    inserted = 0
    #ask for more money
    while inserted < total:
        inserted += eval(input("Deposit a coin or note (in cents):\n"))
        #calculate change
    if inserted > total:
        sum = inserted - total
        if sum != 0:
            print("Your change is:")
        dollars = sum//100
        if dollars != 0:
            print(dollars,'x $1')
        small_dollars = (sum - dollars*100)//25
        if small_dollars != 0:
            print(small_dollars,'x 25c')
        ten_cents = (sum - dollars*100 - small_dollars*25)//10
        if ten_cents != 0:
            print(ten_cents,'x 10c')
        five_cents = (sum - dollars*100 - small_dollars*25 - ten_cents*10)//5
        if five_cents != 0:
            print(five_cents,'x 5c')
        one_cents = (sum - dollars*100 - small_dollars*25 - ten_cents*10 - five_cents*5)//1
        if one_cents != 0:
            print(one_cents,'x 1c')

change_calc()