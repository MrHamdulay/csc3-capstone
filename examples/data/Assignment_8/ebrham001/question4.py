'''Recursive function finding all palindromic primes between two numbers
HAMZA EBRAHIM
09/05/2014'''

# Assignment 8 - Question 4

import sys
sys.setrecursionlimit (30000)

# recursive function which checks for a palindrome

def palindrome(s):
    
    if len(s) == 1 or len(s) == 0:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])

# recursive function which checks for a prime number
    
def prime(z, y):
    
    if z == 1 or z == 0:
        return False
    elif z == 2 or z == 3:
        return True
    elif z % y == 0 and y > 1:
        return False
    elif y > 3:
        return prime(z, y- 1)
    else:
        return True
    
# recursive function that finds both palindromic and prime numbers

def palinprimes(n, m):
    
    p = palindrome(str(n))
    y = n // 2
    z = prime (n, y)
    if n == m + 1:
        return 0
    elif z == True and p == True:
        print(n)
        palinprimes(n+1, m)
    else:
        return palinprimes(n+1, m)
    
# prompt user for start and end points    
    
n = eval(input("Enter the starting point N:\n"))    
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palinprimes(n,m)

# program ends