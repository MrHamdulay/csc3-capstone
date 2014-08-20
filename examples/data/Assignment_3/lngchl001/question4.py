n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
def prime(n):
    if n==2: return True
    if n==3: return True
    if n%2==0: return False
    if n%3==0: return False
    for p in range(3,int(m**(1/2)+1),2):
        if n==p and n%p==0: return True
        if n%p==0: return False
    else: return True
    
def palin(x):
    p=''
    while x:
        x,p=x//10,(p+str(x%10))
    return int(p)
print("The palindromic primes are:")
for i in range(n+1,m):
    #prime(i)
    if prime(i)==True:
        #palin(i)
        if palin(i)== i:
            print(i)
            

