"""recursive program to find all palindromic primes between two integers supplied as input
tafara mtutu
06 may 2014"""

import sys
sys.setrecursionlimit (30000)
import math

def palindrome(n, m):
    if n == m+1:
        return ""
    elif n == 2:
        print(n)
    
    else:
        if prime_check(n, 2):
            if str(n) == check(str(n)):            
                print(n)
    return palindrome(n+1, m)

def prime_check (prime, divisor):
    if prime == 1:
        return False
    elif divisor > math.sqrt(prime):
        return True
    
    else: 
        if prime%divisor == 0:
            return False
        else:
            return prime_check(prime, divisor+1)
        
def check (sentence):
    if len(sentence) == 1:
        return sentence
    else:
        return sentence[-1] + check(sentence[:-1])
        
        
lower = input("Enter the starting point N:\n")
if lower :
    upper = input("Enter the ending point M:\n")
    if upper:
        print("The palindromic primes are:")
        palindrome(eval(lower), eval(upper))
    
            