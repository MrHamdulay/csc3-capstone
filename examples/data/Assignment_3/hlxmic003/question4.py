# Michaela Heale
# Assignment 3 Question 4

import math

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

lister = ""

def isprime(n):
    n = int(n)
    if n<2:
        return False
    if n == 2:
        return True
    if not n&1:
        return False
    for p in range(3,(n//2)+1,2):
        if n%p == 0:
            return False
    return True

for z in range (N+1,M,1):  
    if isprime(z):
        stringz = str(z)
        lng = len(stringz)
        back = int(stringz[::-1])
        if back==z:
            lister += stringz+"\n"

print("The palindromic primes are:",lister,sep="\n")