#AMNTAS003  #Tashfia Amin   #Due Date: 9 May 2014
#Question 4: Assignment 8   #Check for palindromic primes using recursion

import sys
sys.setrecursionlimit (30000)
import math

#Create variables with input for range of numbers
N = eval(input("Enter the starting point N: \n"))
M = eval(input("Enter the ending point M: \n"))


def check(N,div):
    if div == round(math.sqrt(N)):                                 #stop dividing when denominator is equal to the numerator(stops recursion)
        return 0
    if N%div != 0 :                                                #if no remainder, add one and run through next denominator                
        return 1 + check(N, ((div)+1))
    if N%div == 0 :                                                #if remainder, run through next denominator
        return 0 + check(N, ((div)+1))
    
def reverse(N):
    N = str(N)
    if len(N) == 1:
        return N
    else:
        return reverse(N[1:])+N[0]
    
def palindromic_primes(N, M):
    if N == M :
        if check(N,2) == (round(math.sqrt(N))-2):
            print(N)
        else:
            return 0
    elif N == 4 or N == 6 or N == 9 or N == 10201:
        print("", end="")
        palindromic_primes((N+1),M)
    elif str(N) == reverse(N):                                      #check if number is a palindrome
        if N == 1 and M >= 3:
            palindromic_primes((N+1),M)
        elif 1 < N <= 2 and M >= 3:
            print(2)
            palindromic_primes((N+1),M)
        elif check(N,2) == (round(math.sqrt(N))-2):                 #check if number is a prime and has no other factors by running through check_prime function
            print(N)                                                #print number if palindromic prime
            palindromic_primes((N+1),M)                             #run for next number between n and m
        elif check(N,2) != (round(math.sqrt(N))-2):                 #if number if not a prime
            palindromic_primes(N+1,M)                               #run for the next number
    
    else:
        palindromic_primes((N+1),M)       

print("The palindromic primes are:")
palindromic_primes(N, M)