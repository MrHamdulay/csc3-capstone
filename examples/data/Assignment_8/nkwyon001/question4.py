"""program to find all palindromic primes between two integers supplied as input 
Yondela Nkwali
06 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)

def reverse(no):
    numb=str(no)
    if no == "":
        return ""
    else:
        return numb[-1] + reverse(numb[:-1])   
"""def isPrime(n):
    if n%n == 1 and n%1 == 1:
        return true
    else:
        return false"""
x= round(math.sqrt(M))
"""def devis(s):
    if  2<=s<=x:
        return s"""
def devis(s):
    if s == 2:
        return 2
    else:
        return s%2 + devis(s-1)                                                                                             
    if s == x:
        return x
    d=devis()
def isPrime(n):
    if n == 0:
        return false
    if n == 1:
        return false
    else:
        value= n // prime(n - 1)
        if value != 0:
            return false
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if isPrime(n) and len(str(n))>1:
    print(n)