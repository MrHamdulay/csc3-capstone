N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    for j in range(2,i):
        if i%j==0:break
    else:
        i=str(i)
        rev=i[::-1]
        if i==rev:
            print(i)
