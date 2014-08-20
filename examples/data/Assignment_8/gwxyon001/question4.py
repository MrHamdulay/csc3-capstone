'''Name: Yongama Giwu
Program to calculate prime numbers that are palindromes'''
import sys
sys.setrecursionlimit (30000)

import math

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

def palindrome(pal):
    pal = str(pal)
    if len(pal)==1 or pal=='':
        return True

    elif pal[0]!=pal[-1]:
        return False

    else:
        return palindrome(pal[1:-1])

def prime(N,s):
    if N==1:
        return False
    elif s>math.sqrt(N):
        return True

    elif N%s==0:
        return False

    else:
        return prime(N,s+1)

def PalPrime(N,M):
    if N>M:
        print('')
    elif palindrome(N):
        if prime(N,2):
            print(N)
            PalPrime(N+1,M)
        else:
            return PalPrime(N+1,M)
    else:
        return PalPrime(N+1,M)

print("The palindromic primes are:")
sua=PalPrime(N,M)








