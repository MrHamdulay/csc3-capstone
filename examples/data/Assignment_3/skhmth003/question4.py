N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for c in range(N+1,M):
        PrimeNumber = True
        for i in range(2,200):
                if c!=i and (c%i==0):
                        PrimeNumber = False
        if PrimeNumber:
                c=str(c)
                d=c[::-1]
                if c==d:
                        print(c)