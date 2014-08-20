N=eval(input("Enter the starting point N:\n"))

M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def prime(x):
    if x%2==0 and x>2:
        return False
    for i in range(3, x//2, 2):
        if x%i==0:
            return False
    return True
    
for i in range(N+1, M):
    i=str(i)
    if i[::-1]==i:
        x=eval(i)
        if prime(x):
            print(x)