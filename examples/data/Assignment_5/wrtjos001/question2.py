#Assignment 5 Question 2
#WRTJOS001 Joshua Wort
#13 April 2014

cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
total=0
count=0
while total<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    total+=deposit
    count+=1
change=total-cost
if change>0:
    print("Your change is:")
dollars=change//100
if dollars>=1:
    print(dollars,"x $1")
    change-=dollars*100
    twenty_five_cents=change//25
    if twenty_five_cents>=1:
        print(twenty_five_cents,"x 25c")
        change-=twenty_five_cents*25
        ten_cents=change//10
        if ten_cents>=1:
            print(ten_cents,"x 10c")
            change-=ten_cents*10
            five_cents=change//5
            if five_cents>=1:
                print(five_cents,"x 5c")
                change-=five_cents*5
                one_cents=change//1
                if one_cents>=1:
                    print(one_cents,"x 1c")
else:
    twenty_five_cents=change//25
    if twenty_five_cents>=1:
            print(twenty_five_cents,"x 25c")
            change-=twenty_five_cents*25
            ten_cents=change//10
            if ten_cents>=1:
                print(ten_cents,"x 10c")
                change-=ten_cents*10
                five_cents=change//5
                if five_cents>=1:
                    print(five_cents,"x 5c")
                    change-=five_cents*5
                    one_cents=change//1
                    if one_cents>=1:
                        print(one_cents,"x 1c") 
    else:
        ten_cents=change//10
        if ten_cents>=1:
            print(ten_cents,"x 10c")
            change-=ten_cents*10
            five_cents=change//5
            if five_cents>=1:
                print(five_cents,"x 5c")
                change-=five_cents*5
                one_cents=change//1
                if one_cents>=1:
                    print(one_cents,"x 1c")
        else:
            five_cents=change//5
            if five_cents>=1:
                print(five_cents,"x 5c")
                change-=five_cents*5
                one_cents=change//1
                if one_cents>=1:
                    print(one_cents,"x 1c")
            else:
                one_cents=change//1
                if one_cents>=1:
                    print(one_cents,"x 1c")                
                