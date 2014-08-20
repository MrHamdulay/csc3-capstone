N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(N+1,M):
    n = str(i)
    prime = True
    for t in range(2,i):
        if (i%t==0):
            prime = False
    if (prime and n==n[::-1] and i>=2):
        print(i)