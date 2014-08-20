"""find all prime palindromes between two integers
Paul Truter
08 May 2014"""

import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

def PalindromePrime(N,M):
    if N == M:
        if isPrime(N,divisor=2) and isPalindrome(str(N)):
            print(N)
        else:
            return
    else:
        if isPrime(N,divisor=2) and isPalindrome(str(N)):
                print(N)
                PalindromePrime(N+1,M)
        else:
            PalindromePrime(N+1,M)
    

def isPalindrome(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])


def isPrime(s,divisor=2):
    if s == 0:
        return False
    elif s == 1:
        return False
    elif  divisor > s//2:
        return True
    elif s % divisor == 0:
        return False
    else:
        divisor+=1
        return isPrime(s,divisor)
    
#PalindromePrime(N,M)
print("The palindromic primes are:")
PalindromePrime(N,M)