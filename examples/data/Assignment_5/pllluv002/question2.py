c=eval(input("Enter the cost (in cents):\n"))
if c!= 0:
    b=eval(input("Deposit a coin or note (in cents):\n"))
    z=b
    if c>z:
        while c>z:
            d=eval(input("Deposit a coin or note (in cents):\n"))
            z=z+d
    if c<z:   
        print("Your change is:")
        a=z-c
        #1$
        e=a//100
        if e>0:
            print(e,"x $1")
        
        #25c
        f=a-(e*100)
        g=f//25
        if g>0:
            print(g,"x 25c")
        
        #10c
        h=f-(g*25)
        i=h//10
        if i>0:
            print(i,"x 10c")
        
        #5c
        j=h-(i*10)
        k=j//5
        if k>0:
            print(k,"x 5c")
        
        #1c
        l=j-(k*5)
        if l>0:
            print(l,"x 1c")
        
    
    
