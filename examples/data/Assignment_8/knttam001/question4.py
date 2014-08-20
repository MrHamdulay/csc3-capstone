"""Program to Find All the Palindromic Primes Between Two Integers Using Recursion
Tamsin Kantor
May 2014"""

import math 
import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def reverse_order(N): # reverse the order of a string
    N = str(N)  
    if len(N) == 1: # base case to end recursion
        return N
    else:
        return reverse_order(N[1:]) + N[0]

def is_prime (N,factor): # test to see if a number is prime
    if factor == round(math.sqrt(N)) + 1: # base case to end recursion - number is prime
        return True
    elif N % factor != 0 : # if there is a remainder - continue testing               
        return is_prime(N, factor + 1)
    elif N % factor == 0 : # base case to end recursion - number isn't prime
        return False    
    
def palinprime_test(N,M): # test for palindromic primes
    if N < M: # if it is not the last number to test
        if str(N) == reverse_order(N): # test for a palindrome
            if is_prime(N,2) == True: # test for a prime
                if N != 1: # if it is a prime - print
                    print(N)
                return palinprime_test(N+1,M)
            elif is_prime(N,2) == False: # if it isn't a prime - don't print
                return palinprime_test(N+1,M)
        elif str(N) != reverse_order(N):
            return palinprime_test(N+1,M)
    else: # if it is the last number to test
        if str(N) == reverse_order(N):
            if is_prime(N,2) == True:
                print(N)        

# run the function
palinprime_test(N,M)    