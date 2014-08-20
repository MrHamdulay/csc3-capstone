#Akhil Singh
#13 April 2014
#Assignment 5
#Question 2

cost= eval(input("Enter the cost (in cents):\n"))

#deposit=eval(input("Deposit a coin or note (in cents):\n"))
total=0 
while total < cost and cost!=0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    total+=deposit
if total > cost:
    change=total-cost
    print("Your change is:")
    one_dollar=0
    quarter=0
    ten_cents=0
    five_cents=0
    one_cent=0
    while change > 0:
        if change/100 >=1:
            one_dollar=change//100
            change=change-(one_dollar*100)
        if change/25 >=1:
            quarter=change//25
            change=change-(quarter*25)
        if change/10 >=1:
            ten_cents=change//10
            change=change-(ten_cents*10)
        if change/5 >=1:
            five_cents=change//5
            change=change-(five_cents*5)
        if change/1 >=1:
            one_cent=change/1
            change=change-(one_cent*1)
        if one_dollar:
            print(one_dollar,"x $1")
        if quarter:
            print(quarter,"x 25c")
        if ten_cents:
            print(ten_cents,"x 10c")
        if five_cents:
            print(five_cents,"x 5c")
        if one_cent:
            print(one_cent,"x 1c")
        
    
    