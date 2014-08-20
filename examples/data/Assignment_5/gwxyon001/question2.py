"""Yongama Giwu 16 April 2014"""


def change():
    cost = eval(input("Enter the cost (in cents):\n"))
    Deposit = 0
    while Deposit < cost:
        Deposite = eval(input("Deposit a coin or note (in cents):\n"))
        Deposit += Deposite
        
    if Deposit > cost:    
        change = Deposit - cost
        remainder = change % 100
        remainder_1 = remainder % 25
        remainder_2 = remainder_1 % 10
        remainder_3 = remainder_2 % 5 
        print("Your change is:")
        if change >= 100:
            factor_1 = int(change / 100)
            print(factor_1 ,"x $1")
        if remainder >= 25:
            factor_2 = int(remainder / 25)
            print(factor_2 ,"x 25c")
        if remainder_1 >= 10:
            factor_3 = int(remainder_1 / 10)
            print(factor_3 ,"x 10c")
        if remainder_2 >= 5:
            factor_4 = int(remainder_2 / 5)
            print(factor_4 ,"x 5c")
        if remainder_3 >= 1:
            factor_5 = int(remainder_3 / 1)
            print(factor_5 ,"x 1c")
    
change()
    

