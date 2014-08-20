def prime(x):
    if x!=2:
        for i in range(2,x):
            if x%i ==0:
                z= "not prime"
                break
            else: z = "prime"
    else: z="prime" 
    return z


N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")


for i in range(N+1,M):
    y = str(i)
    if y==y[ : :-1]:
        if prime(i)== "prime":
            print(i)

