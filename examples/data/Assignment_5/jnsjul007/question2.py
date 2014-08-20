def main():
    cost=eval(input("Enter the cost (in cents):\n"))
    money=0   
    q= 0
    w= 0
    e= 0
    r= 0
    t= 0
    
    while money<cost:
        x = eval(input("Deposit a coin or note (in cents):\n"))
        money = money + x
    change = money - cost
    if change == 0:
        print("",end = "")
    else:
        while change>0:
            if change>=100:
                q+=1
                change-=100
            elif change>=25:
                w+=1
                change-=25
            elif change >= 10:
                e+=1
                change-=10
            elif change >= 5:
                r+=1
                change-=5
            elif change >= 1:
                t+=1
                change-=1
       
        print("Your change is:")
        if q != 0:
            print(str(q) + " x $1")
        if w != 0:
            print(str(w) + " x 25c")
        if e != 0:
            print(str(e) + " x 10c")
        if r != 0:
            print(str(r) + " x 5c")
        if t != 0:
            print(str(t) + " x 1c")
main()