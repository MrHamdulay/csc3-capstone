N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range (N+1,M):
    for j in range(2,i):
        if i%j==0:
            #print("not prime")
            break
        elif i==1:break
    else:
        p=str(i)
        q=p[-1::-1]
        e=eval(q)
        if e==i: 
            print(p)
            
            
                