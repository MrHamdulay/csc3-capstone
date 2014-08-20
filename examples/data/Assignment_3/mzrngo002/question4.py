n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def prime(n):
    for x in range(2,n):
        y=n%x
        if y==0: 
            return False
    return True

def check(p):
    p=str(p)
    l=len(p)-1
    rp=p[l::-1]
    x=int(p)
    y=int(rp)
    if y==x:
        return True
    return False

for a in range(n+1, m):
    if prime(a) and check(a):
        print(a)