N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    value=str(i)
    check=value[::-1]
    if check==value:
        t=2
        test=0
        while t<i:
            test=i%t
            t+=1
            if test==0: break
        if test!=0:
            print(i)
        if i==2:
            print(i)
        
        
        