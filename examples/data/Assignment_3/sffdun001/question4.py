N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
while N<(M-1):
    N=N+1
    n=str(N)
    if n==n[-1::-1]:
        prime=0
        for i in range (1,N):
            if N%i==0:
                prime=prime+1
                if prime>1:
                    break
        if prime==1:
            print(N)
    else: continue 
   