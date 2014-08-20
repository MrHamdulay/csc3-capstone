'''Joshen Credelio Jacob
08/05/2014
palindromic prime numbers'''

import math

a=eval(input('Enter the starting point N:\n'))
b=eval(input('Enter the ending point M:\n'))

def ispalindrome(x):
    if len(x) < 2:
        return True
    elif x[0]==x[-1]:
        return ispalindrome(x[1:-1])
    else:
        return False
    
def isprime(y,z):
    if y <= 1:
        return False 
    
    elif z > y:
        return True
    
    elif y%z==0 and y > z:
        return False 
    
    else:
        return isprime(y,z+1)
    
def palindrome_primes(a,b):
    if a <= b:
        if isprime(a,2) == True:
            if ispalindrome(str(a)) == True:
                print(a)
                return palindrome_primes(a+1,2)
            else: 
                palindrome_primes(a+1,2)
        else:
            return palindrome_primes(a+1,2)
    else:
        return 0

        
print('The palindromic primes are:')
palindrome_primes(a,b)