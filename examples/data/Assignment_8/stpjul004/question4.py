""" Program to check for palindromic primes
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-05-09 """

import sys

from math import *

sys.setrecursionlimit (30000)

n = eval(input("Enter the starting point N:\n"))

m = eval(input("Enter the ending point M:\n"))

def check_prime(num,den):
    # Divisible by 1
    if den == 1:
        return True
    # If it is divisible by a number other than itself
    elif num%den == 0:
        return False
    # Recursive Step. Otherwise check for the next value
    else:
        return check_prime(num,den-1)
    
def check_palin(s):
    if (len(s) <= 2) and (s[0] == s[len(s)-1]): 
        #If it has made it this far it must be a palindrome!
        return True
        
    # If the string is longer than 2:
    # Check if the outermost characters are the same. 
    elif s[0] == s[len(s)-1]:
        #Recursive step. Remove the outermost characters and pass it on.
        return check_palin(s[1:len(s)-1])
        
    #(B) Terminating step. If all else fails it is not a palindrome
    else:
        return False

def palin_prime(n,m):
    # Terminating step if the value is out of range return an empty string
    if n > m:    
        return ''
    # Otherwhise if the value is both a prime and a palindrome print it out
    elif check_prime(n,trunc(sqrt(n))) and check_palin(str(n)) and n > 1:
        print(n)
        # (A) Recursive step. repeat process for the next value 
        return palin_prime(n+1, m)
    else:
        # (B) Recursive Step. 
        # If the value is neither a palindrome nor a prime, move on.
        return palin_prime(n+1, m)
    

print("The palindromic primes are:")
palin_prime(n,m)