def checkPrime(a):
    a = abs(int(i))
    if a < 2:
        return False
    if a == 2:
        return True
    if not a & 1:
        return False
    for x in range(3, int(a**0.5)+1,2):
        if a % x == 0:
            return False
    return True
    

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range (n,m):
    if (str(i) == str(i)[::-1]) and (checkPrime(i) == True):
        if (i != n) and (i != m):
            print(i)
        
        
        