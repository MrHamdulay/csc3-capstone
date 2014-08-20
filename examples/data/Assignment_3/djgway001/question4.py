#finding palindromic primes

a=eval(input("Enter the starting point N:\n"))
b=eval(input("Enter the ending point M:\n"))

print('The palindromic primes are:')
for x in range (a+1,b):
    prime=True
    for y in range(2,x):
        if x%y==0:
            prime=False
            break
    if prime==True:
        y=str(x)
        z=str(x)[::-1]
        if y==z:
            print(x)
        else: continue
    

