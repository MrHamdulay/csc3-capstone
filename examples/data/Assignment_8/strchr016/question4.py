"""Checking for palindromic prime numbers
Christopher Sterley
04/05/2014"""

import question1 #to use palindrome_checker
import math
import sys
sys.setrecursionlimit (30000) #to increase the number of allowable recursions

lower_boundary=eval(input("Enter the starting point N:\n")) #getting lower boundary input

upper_boundary=eval(input("Enter the ending point M:\n"))   #getting upper boundary input


def prime_finder(divisor,number): #function that returns value 2 for non-primes and 1 for primes
    factors=0

    if divisor>math.sqrt(number):
        return 0
    elif factors>2:
        return 0
    elif number%divisor==0:
        return factors+ 1 + prime_finder(divisor+1,number)
    else:
        return factors + prime_finder(divisor+1,number)


def range_cycler(lower_boundary,upper_boundary): #function that cycles through the given range and checks for palindromic primes
    
    if lower_boundary>upper_boundary:
        return 0
    else:
        if prime_finder(1,lower_boundary)==1 and str(lower_boundary)==(question1.palindrome_checker(str(lower_boundary),len(str(lower_boundary))-1)) and lower_boundary!=1:
            print(lower_boundary)
            return range_cycler(lower_boundary+1,upper_boundary)
        else:
            return range_cycler(lower_boundary+1,upper_boundary)

print("The palindromic primes are:")
range_cycler(lower_boundary,upper_boundary)
        