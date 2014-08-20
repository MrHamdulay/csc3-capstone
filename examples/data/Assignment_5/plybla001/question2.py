cost=eval(input("Enter the cost (in cents):\n"))
change=0
while cost>0:
    dep = eval(input("Deposit a coin or note (in cents):\n"))
    cost-= dep
    if cost<0:
        change=abs(cost)
else: 
    dol = change//100
    num1=change%100
    t5=num1//25
    num2=num1%25
    ten=num2//10
    num3 = num2%10
    five = num3//5
    cents=num3%5
    
    if change>0:
        print("Your change is:")
        if dol !=0:
            print(dol,"x $1")
        if t5 !=0:
            print(t5,"x 25c")
        if ten!=0:
            print(ten,"x 10c")
        if five !=0:
            print(five,"x 5c")
        if cents !=0:
            print(cents,"x 1c")
    