""" Assignment 5 - question 2
zaheer mahmood
16-04-2014"""

cost =eval(input("Enter the cost (in cents):\n"))

if cost!=0:
    deposit_1=eval(input("Deposit a coin or note (in cents):\n"))
    while deposit_1<cost:
        deposit_1+=eval(input("Deposit a coin or note (in cents):\n"))
    change=deposit_1-cost
    if change!=0:
        print("Your change is:")
        count=0
        while change>=100:
            change-=100
            count+=1
        if count!=0:
            print(count, "x", "$1")
        count=0
            
        while change>=25:
            change-=25
            count+=1
        if count!=0:
            print(count, "x", "25c")
        count=0
        while change>=10:
            change-=10
            count+=1
        if count!=0:
            print(count, "x", "10c")
        count=0
        while change>=5:
            change-=5
            count+=1
        if count!=0:
            print(count, "x", "5c")
        count=0
        while change>=1:
            change-=1
            count+=1
        if count!=0:
            print(count, "x", "1c")