N=(eval(input("Enter the starting point N:\n"))+1)
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def primetest(i):
    if i==1:
        return False
    if i==2:
        print(i)
    if not i & 1:
        return False
    for a in range(3, int(i**0.5)+1, 2):
        if i % a ==0:
            return False
    print(i)
    
    
i=N
for i in range(N,M):
    if str(i)[::-1] == str(i):
        primetest(i)
    else:
        i=i+1