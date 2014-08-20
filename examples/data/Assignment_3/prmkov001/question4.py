
from math import *

def palin(x):
    return str(x) == str(x)[::-1]

def isprime(x):
    for j in range(2, int(floor(sqrt(x))) + 1):
        if x % j == 0:
            return False
    return True

a = int(input('Enter the starting point N:\n'))
b = int(input('Enter the ending point M:\n'))

print('The palindromic primes are:')

for i in range(a + 1, b):
    if isprime(i) and palin(i):
        print(i)

