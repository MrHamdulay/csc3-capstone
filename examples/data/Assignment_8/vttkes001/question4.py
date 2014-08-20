"""Program to check for palindromic primes
Keshin Vittee
5 May 2014"""

import math
import question1
import sys
sys.setrecursionlimit (30000)

def is_prime(x, divisor):
    if x < 2: # cannot be prime number if smaller than 2
        return False
    
    elif x ==2:
        return True # 2 is the first prime number
        
    elif math.sqrt(x) + 1 > divisor: 
        if x % divisor == 0:
            return False # not a prime number
        else:
            return is_prime(x, divisor + 1)
    else:
        return True
    
def counter(N, M):
    if N <= M:
        if is_prime(N, 2) and question1.palindrome(str(N)):
            print(N)
        counter(N+1, M)
        

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
counter(N, M)