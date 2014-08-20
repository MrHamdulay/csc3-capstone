N=eval(input("Enter the starting point N:\n"))
N=N+1
M=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(N,M):
    j=str(i)    
    reverse=j[::-1]
    
    if i<2:
        prime=False
    else:
    
        for k in range(2,i):
            if i%k!=0:
                prime=True
            else:
                prime=False
                break
    if i==2:
        prime=True
        
    if j==reverse and prime and i!=1:
        print(i)


    