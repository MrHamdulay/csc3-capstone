""""Palindromic Primes using Recursion
Adam Edelberg
2014/05/09"""

import sys
sys.setrecursionlimit (30000)

from math import sqrt


N = eval(input("Enter the starting point N:\n"))

M = eval(input("Enter the ending point M:\n"))

def prime (N,M):
    if N <= 1:
        return False
    if M == 1:
        return True
    
    if N == 0:
        return False
    
    if N%M != 0:
        return prime(N,M-1)
    else:
        return False
    
def palindrome(num):
 
    if len(num) <= 1:
        return True
    if num[0] == num [-1]:
        return palindrome(num[1:-1])
    else:
        return False


def printer(N,M):
    
    if N>M:
        return ""
    
    if prime(N,sqrt(N)//1) and palindrome (str(N)):
        return str(N)+"\n" + printer(N+1, M)
    
    else:
        return printer(N+1,M)

print("The palindromic primes are:\n", printer(N,M),sep="")