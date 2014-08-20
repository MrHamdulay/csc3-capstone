def isprime(a):
    for i in range (2,a-1):
        if a%i==0:
            return False
    return True
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
for i in range (N+1,M):
    if isprime(i) and str(i)== (str(i))[::-1]:
        print(i)        