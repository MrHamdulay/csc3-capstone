"""program to find palindromic primes between 2 integers
nosipho khumalo
04 May 2014"""

import  math
import sys
sys.setrecursionlimit (30000)

def palindrome(n):
    n = str(n)
    if len(n) <= 1:
        return True
    elif (ord(n[0]) - ord(n[len(n)-1])) == 0:
        return palindrome(n[1:len(n)-1])
    else:
        return False

def prime(n, i):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % i == 0 and i<= math.ceil(n**0.5):
        return False
    elif n % i == 0 and i == n:
        return True
    elif n % i != 0 and i <= math.ceil(n**0.5):
        i += 1
        return prime(n, i)
    elif n % i != 0 and i >= math.ceil(n**0.5):
        return True
    elif n >1:
        i += 1
        return prime(n, i)

def prog(n, m):
    if n <= m:
        if (palindrome(n) == True):
            if prime(n, i) == True:
                print(n)
        return prog(n+1, m)

    
n = eval(input("Enter the starting point N: \n"))
m = eval(input("Enter the ending point M: \n"))
i = 2
print("The palindromic primes are:")
prog(n, m)    