cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
while deposit<cost:
    deposit+=eval(input("Deposit a coin or note (in cents):\n"))
change=deposit-cost
if change>0:
    print("Your change is:")
    d=change//100
    d1=change%100
    q=d1//25
    q1=d1%25
    t=q1//10
    t1=q1%10
    f=t1//5
    f1=t1%5
    if d!=0:
        print(d,"x $1")
    if q!=0:print(q,"x 25c")
    if t!=0:print(t,"x 10c")
    if f!=0:print(f,"x 5c")
    if f1!=0:print(f1,"x 1c")

    

