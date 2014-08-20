def prime():
    N=input("Enter the starting point N:\n")
    M=input("Enter the ending point M:\n")
    m=eval(M)
    n=eval(N)
    print("The palindromic primes are:")
    for i in range(n,m):
        ex=str(i)
        if ex[::-1]==ex:
            x=eval(ex)
            a=2
            if x!=n:
                if x==2:
                    print(x)
                for i in range(2,x):
                    if x%2!=0:
                        b=x%a
                        if b!=0:
                            a+=1
                            b=x%a
                            if a==x:
                                print(x)
                        
                        
prime()

                
                