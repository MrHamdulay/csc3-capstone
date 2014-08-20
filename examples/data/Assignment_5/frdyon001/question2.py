"""Program to calculate change given
Tumi Mkhawana
15 April 2014"""

#input the cost
cost=eval(input("Enter the cost (in cents):\n"))
if cost==0:
    ""
else:
    new_deposit=0
    while True:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        new_deposit+=deposit
        if new_deposit>=cost:
            break
    left_over_deposit=new_deposit-cost
    if left_over_deposit==0:
        ""
    else:
        #print the change
        print("Your change is:")
        dollar=left_over_deposit//100
        twenty_five=(left_over_deposit-(100*dollar))//25
        ten=(left_over_deposit-(100*dollar)-(25*twenty_five))//10
        five=(left_over_deposit-(100*dollar)-(25*twenty_five)-(10*ten))//5
        one=(left_over_deposit-(100*dollar)-(25*twenty_five)-(10*ten)-(5*five))//1
        if dollar!=0:
            print(dollar,"x $1")
        if twenty_five!=0:
            print(twenty_five,"x 25c")
        if ten!=0:
            print(ten,"x 10c")
        if five!=0:
            print(five,"x 5c")
        if one!=0:
            print(one,"x 1c")
