import math

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def findPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return True

for i in range(start+1, end):
    p = str(i)
    q = p[::-1]    
    if p == q:
        if findPrime(i):            
            print(q)