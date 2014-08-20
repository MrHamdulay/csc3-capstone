
from math import *


def isprime(y):
    if y <= 1:
        return False
    if y == 2 or y == 3:
        return True
    for i in range(2, int(floor(sqrt(y))) + 1):
        if (y % i == 0):
            return False
    return True

def ispalin(y):
    y = str(y)
    return y == y[::-1]

k = 0

for i in range(eval(input('Enter the starting point N:\n')) + 1, eval(input('Enter the ending point M:\n'))):
    if k == 0:
        print('The palindromic primes are:')
        k += 1
    if ispalin(i) and (isprime(i)):
        print(i)

if k == 0:
    print('The palindromic primes are:')
