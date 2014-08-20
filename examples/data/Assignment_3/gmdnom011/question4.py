# 23 March 2014
# Program to find palindromic primes between two input integers
# by Nomsa Gamedze

import math

def isprime(x):
    if x == 2 or x == 3:
                return True
    elif x == 1:
                return False    
    for e in range(2, int(math.sqrt(x))+1):
        if x % e == 0:
            break
    else: return True

def palin_primes():
    N = eval(input("Enter the starting point N:"'\n'))
    M = eval(input("Enter the ending point M:"'\n'))
    print("The palindromic primes are:")
    for i in range((N+1), M):
        if isprime(i):   
            word = str(i)
            if word == word[::-1]:
                    print(i)
                    
palin_primes()