"""Program to calculate change in cents
Shane Robinson
17 April 2014"""

print("Enter the cost (in cents):")
cost = eval(input())
payment = 0
while payment<cost:
    print("Deposit a coin or note (in cents):")
    payment += eval(input())
else:
    diff = payment-cost
    if diff!=0:
        print("Your change is:")
        diff_1 = diff//100
        if diff_1>0:
            print(diff_1,"x $1")
        else:
            None
        diff = diff-(diff_1*100)
        diff_2 = diff//25
        if diff_2>0:
            print(diff_2,"x 25c")
        else:
            None
        diff = diff-(diff_2*25)
        diff_3 = diff//10
        if diff_3>0:
            print(diff_3,"x 10c")
        else:
            None
        diff = diff-(diff_3*10)
        diff_4 = diff//5
        if diff_4>0:
            print(diff_4,"x 5c")
        else:
            None
        diff = diff-(diff_4*5)
        diff_5 = diff//1
        if diff_5>0:
            print(diff_5,"x 1c")
        else:
            None