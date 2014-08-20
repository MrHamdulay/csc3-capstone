n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def prime(x):
    for i in range(2,x-1):
        a=0              
        if x%i==0:
            break
        else:
            a=1
    if x==2:
        print(x)
    elif a==1:
        print(x)
if n==1:
    print(2)
    print(3)
    for z in range(n+3,m):
        z=str(z)
        b=z[::-1]
        if b==z:
            prime(int(b))     
if n==2:
    print(2)
    print(3)
    for z in range(n+2,m):
        z=str(z)
        b=z[::-1]
        if b==z:
            prime(int(b))    
if n==3:
    for z in range(n+1,m):
        z=str(z)
        b=z[::-1]
        if b==z:
            prime(int(b))    
if n>3:
    for z in range(n,m):
        z=str(z)
        b=z[::-1]
        if b==z:
            prime(int(b))