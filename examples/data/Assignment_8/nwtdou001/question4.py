'''question4.py
prints out list of palindromic primes within user-defined range
douglas newton NWTDOU001
5 may 2014'''

import math
import sys

'''change the recursion limit'''
sys.setrecursionlimit(30000)

'''checks whether string s is a palindrome'''
def pal(s):
    if len(s)==0:
        return True
    return s[0]==s[-1] and pal(s[1:-1])

'''checks whether a number is prime
note that the first factor f is 2 since all numbers have 1 as a factor'''
def prime(n,f=2):
    '''1 is not prime'''
    if n==1: return False
    '''other special case: 2 is prime'''
    if n==2: return True
    
    '''if the factor is more than the square root, then all f pairs checked.
    1 is added in the comparison to cater f'o'r floating point roots'''
    if f>math.sqrt(n)+1:
        return True
    
    '''if f divides into n, then n is clearly not prime'''
    if n%f==0:
        return False
    
    '''current check succeeded, so perf'o'rm next check'''
    return prime(n,f+1)

'''checks 'f'o'r' numbers within [n,m] that are palindromic primes'''
def pal_prime(n,m):
    '''base case is n>m so m can be checked too'''
    if n>m:return None
    if pal(str(n)) and prime(n):
        print(n)
    pal_prime(n+1,m)
    
n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
pal_prime(n,m)