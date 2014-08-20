"""Find palindromic primes
Shane Robinson
4 May 2014"""

import math
import sys
sys.setrecursionlimit(30000)

print("Enter the starting point N:")
N = eval(input())
print("Enter the ending point M:")
M  = eval(input())

def palindrome(num):
    if len(str(num))<2:
        return True
    elif str(num)[0]!=str(num)[-1]:
        return False
    else:
        return palindrome(str(num)[1:-1])

palin_list = []
i = 2

def palin_primes(N, M):
    global i
    if N<=M:
        if palindrome(N):
            if N==2:
                print(N)
                return palin_primes(N+1, M)
            elif N%i==0 or N%2==0 or N==1:
                i = 2
                return palin_primes(N+1, M)
            elif math.sqrt(N)>i:
                i+=1
                return palin_primes(N, M)
            else:
                i = 2
                print(N)
                return palin_primes(N+1, M)
        else:
            return palin_primes(N+1, M)
    else:
        return False

print("The palindromic primes are:")
palin_primes(N, M)
