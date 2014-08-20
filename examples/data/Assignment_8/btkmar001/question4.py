# A program that prints all the palindromic primes within a specified range
# Martin Batek
# 5 May 2014
# No cheating this time...

import sys # Access to system variables
import question1 # For reverse function
import math # For sqrt() function

sys.setrecursionlimit(30000) # Increase recursion limit to 30000

def palindrome_test(number):
    """A function that returns True if the parameter is a palindrome"""
    string = str(number)
    if string == question1.reverse(string):
        return True
    else:
        return False
    
def prime_test(divisor,number):
    """A funtion that returns True if the equal parameter pairs are prime numbers"""
    if number == 1: #For the purpose of this program
        return False
    elif number == 2:
        return True
    elif divisor >= math.sqrt(number) + 1:
            return True    
    elif number%divisor != 0:
        return prime_test(divisor+1,number)
    elif number%divisor == 0:
        return False

    
def palindromic_primes(N,M):
    """A funtion that prints all palindromic primes between and including N and M"""
    if N==M:
        if palindrome_test(N) and prime_test(2,N):
            print(N)
    else:
        if palindrome_test(N) and prime_test(2,N):
            print(N)
            palindromic_primes(N+1,M)
        else:
            palindromic_primes(N+1,M)
            
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_primes(N,M)