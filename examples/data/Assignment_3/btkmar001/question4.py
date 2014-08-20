def isprime(n):
    n = abs(int(n))
    if n<2:
        x = False
    elif n == 2:
        x = True
    elif n%2 == 0 and n !=2:
        x = False
    elif n == 3:
        x = True
    else:
        for i in range(3,n,2):
            if n%i == 0:
                x = False
                break
            else:
                x = True
    return x

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
    a=isprime(i)
    if a==True:
        strprime = str(i)
        backstrprime = strprime[::-1]
        if strprime == backstrprime:
            print(strprime)
            