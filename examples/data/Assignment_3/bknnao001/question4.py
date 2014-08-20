N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:\n")
def Numprime():
    for j in range(N+1,M):
        for f in range(2,M):
            if j%f==0 and f!=j and j!=1:
                break
        else:
            if j != 1:
                print(j)
Numprime()

        