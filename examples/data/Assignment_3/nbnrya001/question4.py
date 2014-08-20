
from math import *

def primenum(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

def palindrome(x):
    x = str(x)
    return x == x[::-1]

n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))

for i in range(n + 1, m):
    if i == n + 1:
        print('The palindromic primes are:')
    if palindrome(i) == True and primenum(i) == True:
        print(i)

if m == n:
    print('The palindromic primes are:')
