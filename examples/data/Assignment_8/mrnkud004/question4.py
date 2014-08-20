"""finding palindromic primes
kennedy muranda
9/5/2014"""

import sys
sys.setrecursionlimit (30000)

#define function to check if number is palindrome
def palind(c):
    if len(c)<2:
        return True
    
    else:
        if c[0]==c[-1]:
            return palind(c[1:-1])
        else:
            return False
        
#check for prime numbers
def is_prime(N):
    
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))



