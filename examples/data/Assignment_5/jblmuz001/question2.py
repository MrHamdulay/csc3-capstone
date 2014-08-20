#q2
y=eval(input("Enter the cost (in cents):\n"))

if y!=0:
    x=eval(input("Deposit a coin or note (in cents):\n"))
    while x<y:
        x+=eval(input("Deposit a coin or note (in cents):\n"))
    k=x-y
    if k!=0:
        print("Your change is:")
        count=0
        while k>=100:
            k-=100
            count=count+1
        if count!=0:
            print(count, "x", "$1")
        count=0
            
        while k>=25:
            k-=25
            count+=1
        if count!=0:
            print(count, "x", "25c")
        count=0
        while k>=10:
            k-=10
            count+=1
        if count!=0:
            print(count, "x", "10c")
        count=0
        while k>=5:
            k-=5
            count+=1
        if count!=0:
            print(count, "x", "5c")
        count=0
        while k>=1:
            k-=1
            count+=1
        if count!=0:
            print(count, "x", "1c")

        