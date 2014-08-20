def prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False
    
x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(x+1,y):
    if prime(i):
        s=str(i)
        if s==s[::-1]:
            print(i)
        else:
            continue
    
