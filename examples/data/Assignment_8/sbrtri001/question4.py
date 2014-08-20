''' Assignment 8, question 4
Use recursive functions to find all palindromic primes between two integers
Tristan Subroyen
7 May 2014 '''

import math
import sys
sys.setrecursionlimit (30000)

def main (num1, num2):
    ''' Executes main program by calling other functions '''
    # base case
    if num1 == num2+1:
        return ""
    elif num1 == 2:
        print(num1)
        
        # recursive step:
    else:
        if checkPrime(num1, 2):
            if str(num1) == checkPalindromic(str(num1)):
                print(num1)
    return main(num1+1, num2)

def checkPrime(num1, num2):
    ''' Checks numbers are prime or not '''
    # base case
    if num1 == 1:
        return False
    elif num2 > math.sqrt(num1):
        return True
    
    # recursive step
    else:
        if num1 % num2== 0:
            return False
        else:
            return checkPrime(num1, num2+1)

def checkPalindromic (string):
    ''' Checks if a given string is palindromic or not '''
    # base case:
    if len(string) == 1:
        return string
    # recursive step
    else:
        return string[-1] + checkPalindromic (string[:-1])

# User inputs:
start = eval(input("Enter the starting point N:\n"))
if start:
    end = eval(input("Enter the ending point M:\n"))
    if end:
        print("The palindromic primes are:")
        main (start, end) 