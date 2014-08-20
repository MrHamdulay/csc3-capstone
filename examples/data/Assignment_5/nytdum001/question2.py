cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
while deposit<cost:
    deposit+=eval(input("Deposit a coin or note (in cents):\n"))
change=deposit-cost
if change>0:
    print("Your change is:")
    d=change//100
    z=change%100
    q=z//25
    x=z%25
    t=x//10
    y=x%10
    f=y//5
    p=y%5
    if d!=0:
        print(d,"x $1")
    if q!=0:
        print(q,"x 25c")
    if t!=0:
        print(t,"x 10c")
    if f!=0:
        print(f,"x 5c")
    if p!=0:
        print(p,"x 1c")