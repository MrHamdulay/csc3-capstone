# question4.py
# Author: Dominic Manthoko
# 27 March 2014

import math

def isPrime(n,m):
    # determine which numbers are prime between the given values
    for n in range(n+1, m):
        for x in range(2, n):
            if n % x == 0:
                break
        # This runs if the number is a prime
        else:
            n0 = str(n)
            if n0 == n0[::-1]:                   # this checks if the prime number is a palindrome
                n1 = int(n0)
                if n1 <2: continue               # any value less than 2 is not a prime, do not print the number       
                else:
                    print(n1)                    # the number printed here is a palindromic prime
                    
if __name__ == '__main__':
    n= eval(input("Enter the starting point N: \n"))
    m = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
        
    isPrime(n,m)