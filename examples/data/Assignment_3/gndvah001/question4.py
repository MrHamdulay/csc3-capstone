n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
i=n+1
print("The palindromic primes are:")
while i<m:
    j=str(i)
    jreverse = j[::-1]
    i=i+1
    if j == jreverse:
        f=eval(j)
        if f > 1:    
            # check for factors
            for k in range(2,f):
                if (f % k) == 0:
                    #print(f,"is not a prime number")
                    #print(k,"times",f//k,"is",f)
                    break
                elif f/k==type(int):
                    print(f,"is a prime number")
            else:
                print(f)
               
        # if input number is less than or equal to 1, it is not prime
        #else:
            #print(f,"is not a prime number")