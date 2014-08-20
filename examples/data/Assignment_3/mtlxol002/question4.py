def primepal(n,m):
    for i in range(n+1,m):
        i=str(i)
        if i == i[::-1]:
            check = prime(eval(i))
            if check == True:
                print(i)
            
            
            
def prime(k):
    if k<2:
        return False
    if k==2:
        return True
    if k%2==0:
        return False
    for x in range(3, k, 2):
        if k % x ==0:
            return False
    return True

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
primepal(N,M)