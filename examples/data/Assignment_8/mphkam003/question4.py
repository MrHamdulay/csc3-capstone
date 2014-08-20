""" print out palindromic prime numbers between a given range
kamogelo mphela 
7 may 2014"""

import sys
sys.setrecursionlimit (30000)
import math
  
def check_palindrome(N):
    """check if a number is palindrome"""
    if N == 1:
        print(N+1)
        return check_palindrome(N+2)
    
    elif N == M + 1:
        return ''
    elif str(N) == str(N)[::-1] and primes(N,2) == 0:
        print(N)
        return str(N) + check_palindrome(N+1)
    else:
        return check_palindrome(N+1)
    
    
N = eval(input ("Enter the starting point N:\n"))

M = eval(input ("Enter the ending point M:\n"))

def primes(N,k):
    """check if a number is a prime"""
    if k>= math.sqrt(N)+1:
        return 0
    elif N%k == 0:
        return 1 
    else:
        return primes(N,k+1)
print ("The palindromic primes are:")
check_palindrome(N)       