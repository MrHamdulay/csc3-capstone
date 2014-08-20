import math
price = eval(input("Enter the cost (in cents):\n"))
payment = eval(input("Deposit a coin or note (in cents):\n"))
while payment<price:
    payment1 = eval(input("Deposit a coin or note (in cents):\n"))
    payment += payment1

countdollar=0
count25=0
count10=0
count5=0
count1=0


if(payment>price):
    change=payment-price
    while (change>=100):
        countdollar=countdollar+1
        change=change-100
    print("Your change is:")
    if(countdollar>=1):
        print(countdollar, "x $1",sep=" ")
            
    while (change>=25):
        count25=count25+1
        change=change-25
    if(count25>=1):
        print(count25, "x 25c",sep=" ")
            
    while (change>=10):
        count10=count10+1
        change=change-10
    if(count10>=1):
        print(count10, "x 10c",sep=" ")    
            
    while (change>=5):
        count5=count5+1
        change=change-5
    if(count5>=1):
        print(count5, "x 5c",sep=" ")    
            
    while (change>=1):
        count1=count1+1
        change=change-5
    if(count1>=1):
        print(count1, "x 1c",sep=" ")               