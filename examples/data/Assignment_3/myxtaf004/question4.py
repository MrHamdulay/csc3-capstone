#starting point n
n=eval(input("Enter the starting point N:\n"))
#the ending point m
m=eval(input("Enter the ending point M:\n"))
def prime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True
print("The palindromic primes are:")
for i in range(n+1, m):
    xs=str(i)
    x=xs[::-1]
    x=int(x)
    if i%x==0 and prime(i):
        print(i)