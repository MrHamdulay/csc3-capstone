"""Recursive function to find palindromic primes
Joseph Preyer
6 May 2014"""

import math
import sys
sys.setrecursionlimit(3000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def prime(N,divisor):
#    print("N is now", N)
    #Base-case: nothing happens if N is greater than M
    if M-N!=-1:
        #Starting number cannot be 0 or 1 or 2
        if N==0 or N==1:
            prime(N+1,2)
        elif N==2:
            print(2)
            prime(N+1,2)
            #Check if palindromic
        elif str(N)==str(N)[::-1]:
            #If number is divisible by current divisor, call function with next starting number
            if N%divisor==0:
                prime(N+1, 2)
            #If divisor is >= the largest possible factor of N, print N, get next N
            else:
                if divisor >= round(math.sqrt(N)):
                    print (N)
                    prime(N+1,2)
                #Else if divisor is not largest possible factor of N, get next divisor
                else:
                    prime(N, divisor+1)
        #Else if N not a palindrome, get next N
        else:
            prime(N+1,divisor)
                              
prime(N,2)