
from math import *

def isprime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, int(floor(sqrt(x))) + 1):
        if (x % i == 0):
            return False
    return True

def ispalin(x):
    x = str(x)
    return x == x[::-1]

a = 0

for i in range(eval(input('Enter the starting point N:\n')) + 1, eval(input('Enter the ending point M:\n'))):
    if a == 0:
        print('The palindromic primes are:')
        a += 1
    if ispalin(i) and (isprime(i)):
        print(i)

if a == 0:
    print('The palindromic primes are:')
