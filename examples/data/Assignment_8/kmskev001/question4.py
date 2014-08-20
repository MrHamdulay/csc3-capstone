"""program to find palindromic primes between two inputed integers
   kevin kumasamba
   09 may 2014"""

import sys
sys.setrecursionlimit (30000)
import math


# problem: finding palindromic numbers that are prime between two numbers
# smaller problem: 1. finding a prime number
#                  2. finding a palindromic number
# to find a palindrome, check if forward integer equal to reverse integer ( convert to string )
# function to find if numbers are prime

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))+1

i=2
def prime(number, i):
    if number==i:
        return True
    elif number%i==0:
        return True + prime(number, i+1)
    elif number%i!=0:
        return prime(number, i+1)

def palin_prime(N, M):
    i=2
    if N==M and N==0:
        return ""
    elif N==1: # important! python goes mad otherwise
        return palin_prime(N+1, M)
    elif N==M:
        if prime(N, i)==True:
            return N
    elif prime(N, i)==True:
        if str(N)==(str(N))[::-1]:
            print(N)
            palin_prime(N+1, M)
        else:
            palin_prime(N+1, M)
    else:
        palin_prime(N+1, M)
            
print("The palindromic primes are:")
palin_prime(N, M)