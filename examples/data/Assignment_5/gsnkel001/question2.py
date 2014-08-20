
#Question 2
#Kelly Goosen
#2014/04/16

cost=eval(input("Enter the cost (in cents):\n")) #get cost of item
if cost == 0: #if there is no cost
    print()
elif cost>=0: #if there is a cost
    payment=eval(input("Deposit a coin or note (in cents):\n")) #while payment is smaller than cost, keep asking for more deposits

    while payment < cost: #once payment smaller than cost
        extra=eval(input("Deposit a coin or note (in cents):\n"))
        payment = extra + payment
    if payment > cost: #once payment is greater than cost
        print("Your change is:")
        change = payment - cost #to calculate change
        remainder = change
        if remainder//100 > 0:
            print(remainder//100,"x $1")
            remainder = remainder%100
        if remainder//25 > 0:
            print(remainder//25,"x 25c")
            remainder = remainder%25
        if remainder//10 > 0:
            print(remainder//10,"x 10c")
            remainder = remainder%10
        if remainder//5 > 0:
            print(remainder//5,"x 5c")
            remainder = remainder%5
        if remainder//1 > 0:
            print(remainder//1,"x 1c")
    


                
