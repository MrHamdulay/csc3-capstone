"""Calculate change in vending machine-Kiara Ramjith-2014"""
cost=eval(input("Enter the cost (in cents):\n"))#get price
if cost>0: #if ifs a valid price continue
    paid=eval(input("Deposit a coin or note (in cents):\n"))
    while(paid<cost):#ask unil amout greater has been entered
        paid=paid+eval(input("Deposit a coin or note (in cents):\n"))
    change=paid-cost
    dol=change//100#interger division
    leftdol=change%100#get the remainder
    tf=leftdol//25#use the remainder and integer divide that
    lefttf=leftdol%25
    t=lefttf//10
    leftt=lefttf%10
    f=leftt//5
    leftf=leftt%5
    if(change>0):
        print("Your change is:")#display only if ther is change
    if(dol>=1):
        print(str(dol)+" x $1")
    if(tf>=1):
        print(str(tf)+" x 25c")
    if(t>=1):
        print(str(t)+" x 10c")
    if(f>=1):
        print(str(f)+" x 5c")
    if(leftf>=1):
        print(str(leftf)+" x 1c")