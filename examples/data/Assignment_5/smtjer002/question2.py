"""A programme to simulate a vending machine
By Jeremy Smith SMTJER002
14 April 2014"""

amount=0
cost=eval(input("Enter the cost (in cents):\n"))
#if no cost is entered, end program
if cost == 0:
    print(end="")
else:
    coin=eval(input("Deposit a coin or note (in cents):\n"))
    amount+=coin
#loop until the deposit is greater than the cost
    while amount < cost:
        coin=eval(input("Deposit a coin or note (in cents):\n"))
        amount+=coin
    change=amount-cost
#calculate and return change
    if change == 0:
        print(end="")
    else:
        print("Your change is:")
        dollar = change//100
        if dollar > 0:
            print(dollar, "x $1")
            change-=dollar*100
        quarter = change//25
        if quarter > 0:
            print(quarter, "x 25c")
            change-=quarter*25
        tencent = change//10
        if tencent > 0:
            print(tencent, "x 10c")
            change-=tencent*10
        fivecent = change//5
        if fivecent > 0:
            print(fivecent, "x 5c")
            change-=fivecent*5
        onecent = change//1
        if onecent > 0:
            print(onecent, "x 1c")
