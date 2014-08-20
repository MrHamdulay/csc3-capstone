'''Vending machine simulator
Mahnoor Ahmed'''

cost=eval(input("Enter the cost (in cents):\n"))
if cost !=0:
    paid=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=paid
    while deposit < cost:
        paid=eval(input("Deposit a coin or note (in cents):\n"))
        deposit=deposit+paid
    else:
        change=deposit-cost
        if change !=0:
            print("Your change is:")
            one_dollar=change//100
            twentyfive_cents=((change%100)//25)
            ten_cents=(((change%100)%25)//10)
            five_cents=((((change%100)%25)%10)//5)
            one_cent=(((((change%100)%25)%10)%5)//1)
        if one_dollar != 0:
            print(one_dollar,"x $1")
        if twentyfive_cents != 0:
            print(twentyfive_cents,"x 25c")
        if ten_cents !=0:
            print(ten_cents,"x 10c")
        if five_cents !=0:
            print(five_cents,"x 5c")
        if one_cent !=0:
            print(one_cent,"x 1c")
    
    
