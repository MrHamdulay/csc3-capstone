#Change pogram
#Gillian Wachira
#19/04/2014

def main():
    c=0
    d=0
    e=0
    f=0
    g=0
    y=eval(input("Enter the cost (in cents):\n"))
    x=0
    while y>x:
        deposit=eval(input("Deposit a coin or note (in cents):\n"))
        x+=deposit
    change=x-y
    if change==0:
        print("",end="")
    else:
        while change>0:
            if change>=100:
                c+=1
                change-=100
            elif change>=25:
                d+=1
                change-=25
            elif change>=10:
                e+=1
                change-=10
            elif change>=5:
                f+=1
                change-=5
            elif change>=1:
                g+=1
                change-=1
        print("Your change is:")
        if c!=0:
            print(str(c)+" x $1")
        if d!=0:
            print(str(d)+" x 25c")
        if e!=0:
            print(str(e)+" x 10c")
        if f!=0:
            print(str(f)+" x 5c")
        if g!=0:
            print(str(g)+" x 1c")
main()