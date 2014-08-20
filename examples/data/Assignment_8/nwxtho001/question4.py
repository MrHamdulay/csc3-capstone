'''program to find all the palindromic primes between two numbers entered by the user
tom new
2014/05/05'''

import question1
import math
import sys
sys.setrecursionlimit (30000)

def divisible (m, n):
    '''checks if a number n is divisble by any integer from a starting point, m, up to n-1; returns boolean value'''
    if n % m == 0: return True # ends when a divisor is found
    elif m >= math.sqrt (n): return False # else ends when no divisor is found before m reaches sqrt (n)
    else: return divisible (m + 1, n) # sends m + 1 to divisible to check the next value
    
def prime (x):
    '''checks if a number is prime; returns boolean value'''
    if x == 1: return False
    if x == 2: return True
    elif not divisible (2, x): return True
    else: return False
    
def palindrome (x):
    '''checks if a number is palindromic; returns boolean value'''
    x = str (x)
    if x == question1.reverse (x): return True
    else: return False

def list_palprimes (m, n):
    '''returns all the palindromic primes between a start and end point as a list'''
    if n == m:
        if palindrome (m) and prime (m): return [m] 
        else: return []
    elif palindrome (m) and prime (m): return [m] + list_palprimes (m + 1, n)
    else: return [] + list_palprimes (m + 1, n)
    
def printlist (l):
    '''prints out all the values in a list, separated by new lines'''
    if len (l) == 1: print (l [0])
    elif len (l) == 0: return
    else:
        print (l [0])
        printlist (l [1:])

if __name__ == '__main__':
    M = eval (input ('Enter the starting point N:\n'))
    N = eval (input ('Enter the ending point M:\n'))
    print ('The palindromic primes are:')
    pps = list_palprimes (M, N)
    printlist (pps)