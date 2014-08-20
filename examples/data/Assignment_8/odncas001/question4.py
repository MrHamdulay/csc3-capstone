"""program to return all palindromic primes between two points using recursion
casey o'donnell
5 may 2014"""

import math
import sys
sys.setrecursionlimit (30000)

def pal_check(s):
    if not s:
        return True    
    elif s[0]==s[-1]:
        return pal_check(s[1:-1])
    else:
        return False

def is_prime(n,i):
    if n==1:
        return False
    elif n%i==0:
        if n==2:
            return True
        else:
            return False
    elif i<round(math.sqrt(n)):
        return is_prime(n,i+1)
    else:
        return True
    
def pal_prime(n,m):
    if n<=m:
        strn=str(n)
        if pal_check(str(n)):
            if is_prime(n,2):
                print(n)
        return pal_prime(n+1,m)
    
n=input("Enter the starting point N:\n")
m=input("Enter the ending point M:\n")
if n:
    print("The palindromic primes are:")
pal_prime(eval(n),eval(m))
                
    