x=eval(input("Enter the cost (in cents):\n"))

if x!=0:
    y=eval(input("Deposit a coin or note (in cents):\n"))
    while y<x:
        y+=eval(input("Deposit a coin or note (in cents):\n"))
    z=y-x
    if z!=0:
        print("Your change is:")
        count=0
        while z>=100:
            z-=100
            count+=1
        if count!=0:
            print(count, "x", "$1")
        count=0
            
        while z>=25:
            z-=25
            count+=1
        if count!=0:
            print(count, "x", "25c")
        count=0
        while z>=10:
            z-=10
            count+=1
        if count!=0:
            print(count, "x", "10c")
        count=0
        while z>=5:
            z-=5
            count+=1
        if count!=0:
            print(count, "x", "5c")
        count=0
        while z>=1:
            z-=1
            count+=1
        if count!=0:
            print(count, "x", "1c")