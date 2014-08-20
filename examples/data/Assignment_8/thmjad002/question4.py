"""Assignment 8, Question 4
JT 
07-05-2014"""

import question1
import math
import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
lst = []
number = 0

def is_palin_prime(n,m):
    if n == m:
        if is_prime(n,2):
            if is_palin(n):
                print(n)
                return True
        else:
            return False
    if is_prime(n,2):
        if is_palin(n):
            print(n)
            return is_palin_prime(n+1,m)
        else:
            return is_palin_prime(n+1,m)
    else:
        return is_palin_prime(n+1,m)
    
    
    
def is_prime(n,i):
    if n == 2:
        return True
    if n == 1:
        return False
    if i == n//2 + 1:
        if n%i != 0:
            return True
        elif n%i == 0:
            return False
    if n%i == 0:
        return False
    elif n%i != 0:
        return is_prime(n,i+1)

def is_palin(n):
    n2 = question1.reverse(str(n))
    if question1.check(str(n),n2):
        return True
    else:
        return False
    
    
    
    
    
    
    
    #if str(n) == str(n)[::-1]:
     #   return True
    #else:
     #   return False

print("The palindromic primes are:")
is_palin_prime(N,M)
    
            