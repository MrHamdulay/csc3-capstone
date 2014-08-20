def palindrome(N,M):
    for i in range (N+1,M):
        j=str(i)
        z=int(round((i**0.5),0))
        Sum=0
        for u in range(2,z+1):
                if i%u==0:
                    u=1
                    Sum+=u
        if Sum==0 and j==j[::-1]:
            print(i)
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindrome(N,M)