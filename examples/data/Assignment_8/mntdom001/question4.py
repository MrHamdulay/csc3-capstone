""" recursive program that finds the palindromic primes between two intergers
Dominic Manthoko
05 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)
from question1 import *

def isPrime(N,div):
    """ a function that determines if a number is prime """
    
    if N <= 1:                            # any number less than or equal to 1 is not a prime number
        return False
    
    elif div >  math.sqrt(N):               # once the divisor is greator than the square root of the number N, then the number is a Prime
        return True
        
    elif N%div == 0:                      # checks if remainder of the number divided by the divisor is zero
        return False                      # returns False if the number isn't a prime
    
    else:
        div+=1
        return isPrime(N, div)          
    
def isPalindrome(N):
    """ function that determines if a number is a Palindrome 
    NB: the reverse funtion from question 1 is used for in this function"""
    
    # convert N to a string
    N = str(N)
    
    if N == reverse(N):              # check if the number is the same as the reverse of the number
        return True                  # return true if the number is a Palindrome
    else:
        return False                 # return False if the number is not Palindrome
    
def isPalin_Prime(N, M):
    """ funtion that finds the palindromic prime numbers between N and M """
   
    if N == M:
        if isPrime(N,2) and isPalindrome(N):      # also check if the last number in the range is a palindrominc prime
            print(N)                              # only print the last number if it is a palindromic prime
        
    elif isPrime(N,2) and isPalindrome(N):        # check if a number is a prime and a palindrome
        print(N)                                  # print out the number if it is a palindromic prime
        N += 1
        return isPalin_Prime(N, M)
    
    else:
        N+= 1
        return isPalin_Prime(N, M)
    
if __name__ == '__main__':
    
    #prompt the user to enter to digits
    N = int(input("Enter the starting point N: \n"))
    M = int(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    isPalin_Prime(N,M)
    