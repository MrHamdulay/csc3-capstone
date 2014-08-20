#Luke Joseph
#JSPLUK001
#2014-04-14
#question 2 of assignment 5
def vending_machine():
    cost=eval(input("Enter the cost (in cents):\n"))
    if cost>0:
        dep=eval(input("Deposit a coin or note (in cents):\n"))
        while cost>dep:
            dep+=eval(input("Deposit a coin or note (in cents):\n"))
        x=dep-cost
        k=dep-cost
        v=str(x)
        a=1
        b=1
        c=1
        d=1
        e=1
        q="r"
        while q=="r":
            while x!=0:
                if x>=100:
                    #print(str(y),"x$1",sep="")
                    x=x-100
                    a+=1
                elif x>=25:
                    #print("1x25c")
                    x=x-25
                    b+=1
                elif x>=10:
                    #print("1x10c")
                    x=x-10
                    c+=1
                elif x>=5:
                    #print("1x5c")
                    x=x-5
                    d+=1
                elif x>=1:
                    #print("1x1c")
                    x=x-1
                    e+=1
                q="s"
            if v=="0":
                break
            else:
                print("Your change is:")
            aw=str(a-1)
            bw=str(b-1)
            cw=str(c-1)
            dw=str(d-1)
            ew=str(e-1)
            while k>0:
                if k>=100:
                    print(aw,"x $1",sep=" ")
                    k-=((eval(aw))*100)
                elif k>=25:
                    print(bw,"x 25c",sep=" ")
                    k-=((eval(bw))*25)
                elif k>=10:
                    print(cw,"x 10c",sep=" ")
                    k-=((eval(cw))*10)
                elif k>=5:
                    print(dw,"x 5c",sep=" ")
                    k-=((eval(dw))*5)
                elif k>=1:
                    print(ew,"x 1c",sep=" ")
                    k-=((eval(ew))*1)
                else:
                    break
vending_machine()
