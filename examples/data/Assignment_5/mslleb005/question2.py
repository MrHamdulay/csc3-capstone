cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
while deposit<cost:
    x=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=x+deposit
if deposit>cost:
    change=deposit-cost
    print("Your change is:")
    a=change//100
    if a>0:
        print(a,"x $1")
    remainder=change%100
    if remainder>0:
        b=remainder//25
        if b>0:
            print(b,"x 25c")
    remainder=remainder%25
    if remainder>0:
        c=remainder//10
        if c>0:
            print(c,"x 10c")
    remainder=remainder%10
    if remainder>0:
        d=remainder//5
        if d>0:
            print(d,"x 5c")
    remainder=remainder%5
    if remainder>0:
        e=remainder//1
        if e>0:
            print(e,"x 1c")
    


                    
    