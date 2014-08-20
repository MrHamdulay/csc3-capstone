"""Assignment 5,Mphuthi Mamorena, April 2014"""

a=eval(input("Enter the cost (in cents):\n"))
if a>0:
    b=0
    # using while to make sure enough coins are deposited
    while b<a:
        b+=eval(input("Deposit a coin or note (in cents):\n"))
    change=b-a
    c=str(change)
    k=int(c)
    # determining change in terms of dollars
    if k!=0:
        if len(c)>0:
            print("Your change is:")
        if len(c)==3 or len(c)==4:
            x=change//100
            print(x,'x','$1')
            d=x*100
            e=change-d
        # determining change in terms of cents
        else:
            e=change
        x=['25','10','5','1']
        if e!=0:
            j=x[0]
            i=int(j)
            f=e//i
            print(round(f),'x',j+'c')
        g=round(f)*25
        n=e-g
        if n!=0:
            l=x[1]
            m=int(l)
            h=n/m
            if round(h)>0:
                print(round(h),'x',x[1]+'c')
    else:
        print()
    


        
    
            