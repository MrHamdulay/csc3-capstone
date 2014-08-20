# question2.py
# a program to simulate a vending machine and calculate change based on the amount paid
# 14 April 2014
# Thomas Konigkramer

def vending_machine():
    """ask for cost"""
    cost = eval(input("Enter the cost (in cents):\n"))
    
    """ask money inserted"""
    deposit = 0
    while deposit < cost: # asks until cost is covered
        deposit += eval(input("Deposit a coin or note (in cents):\n"))
    
    change = deposit - cost
    if change != 0:
        dollars = change // 100
    
        change -= dollars * 100   
        twentyfives = change // 25
    
        change -= twentyfives * 25
        tens = change // 10
    
        change -= tens * 10
        fives = change // 5
    
        change -= fives * 5
        ones = change // 1
    
        """prints output"""
    
        print("Your change is:")
        if dollars > 0:
            print(dollars, "x", "$1")
        if twentyfives > 0:
            print(twentyfives, "x", "25c")
        if tens > 0:
            print(tens, "x", "10c")
        if fives > 0:
            print(fives, "x", "5c")
        if ones > 0:
            print(ones, "x", "1c")

vending_machine()    