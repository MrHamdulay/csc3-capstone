# program that uses recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included).
# Mulisa Badugela
# BDGMUL001
# 08 MAY 2014

import sys
sys.setrecursionlimit (30000)

N =eval(input('Enter the starting point N:\n')) # user input start point

if N == 1 :
    N=N+1

M = eval(input('Enter the ending point M:\n'))   # user input end point
print('The palindromic primes are:')


def palindrome(num):   # function to check for palindrome
    if len(num) <= 1 :
        return True
    else :
        if num[0] == num[len(num)-1]: 
            return palindrome(num[1:len(num)-1])
        else:
            return False
def prime(N,M):   # function to check for primes
    if (M>N**(1/2)):
        return True
    if N%M == 0 : 
        return False
    else:
        return prime(N,M+1)
    
def palindromic_primes(N,M):
    if N>M:
        return ''
    else :
        if palindrome(str(N)) and prime(N,2):
            print(N)
        
        palindromic_primes(N+1,M)


palindromic_primes(N,M)