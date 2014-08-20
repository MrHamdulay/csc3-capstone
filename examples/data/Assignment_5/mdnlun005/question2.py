"""Lungelo Mdunge
Assignment 5 Question2"""


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
            f_1 = int(change / 100)
            print(f_1 ,"x $1")
        if remainder >= 25:
            f_2 = int(remainder / 25)
            print(f_2 ,"x 25c")
        if remainder_1 >= 10:
            f_3 = int(remainder_1 / 10)
            print(f_3 ,"x 10c")
        if remainder_2 >= 5:
            f_4 = int(remainder_2 / 5)
            print(f_4 ,"x 5c")
        if remainder_3 >= 1:
            f_5 = int(remainder_3 / 1)
            print(f_5 ,"x 1c")
    
change()
    

