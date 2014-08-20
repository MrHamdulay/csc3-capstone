N=eval(input('Enter the starting point N:\n'))
M=eval(input('Enter the ending point M:\n'))
i=N+1
print("The palindromic primes are:")
while i<M:
    j=str(i)
    jreverse = j[::-1]
    i=i+1
    if j == jreverse:
        f=eval(j)
        if f > 1:    
            for k in range(2,f):
                if (f % k) == 0:
                    break
                elif f/k==type(int):
                    print(f,"isnt a prime number")
            else:
                print(f)