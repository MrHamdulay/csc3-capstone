"""Question 2, Assignment 5
Vending Machine
Mitchell Holmes
13 April 2014"""

#input cost
cost=eval(input("Enter the cost (in cents):\n"))

if cost>0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    total=0
    sum_of_deposit=total+deposit
# keep asking for more money while input is less than the cost
    while sum_of_deposit < cost:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        sum_of_deposit=sum_of_deposit+deposit


    change=abs(cost-sum_of_deposit)
#count number of returned coins
    count_100=0
    count_25=0
    count_10=0
    count_5=0
    count_1=0

#determine which item of change to give based on amount of change left over
    while change>=100:
        change=change-100
        count_100=count_100+1
    while 25<=change<=99:
        change=change-25
        count_25=count_25+1
    while 10<=change<=24:
        change=change-10
        count_10=count_10+1
    while 5<=change<=9:
        change=change-5
        count_5=count_5+1
    while 1<=change<=4:
        change=change-1
        count_1=count_1+1

# print out the change returned  
    if abs(cost-sum_of_deposit)>0:
        print("Your change is:")
    if count_100>0:
        print(count_100, "x $1")
    if count_25>0:
        print(count_25, "x 25c")
    if count_10>0:
        print(count_10, "x 10c")
    if count_5>0:
        print(count_5, "x 5c")
    if count_1>0:
        print(count_1, "x 1c")
    
    
