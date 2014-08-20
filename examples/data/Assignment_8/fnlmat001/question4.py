# Mathew Finlayson - FNLMAT001
# Assignment 8 - Question 4
# 04/05/2014

import sys
sys.setrecursionlimit (30000)
import math

def revNumber(num):
    """returns the reverse of a number as a string"""
    if num == 0:
        return ""
    else: # gets the last digit and recurses to get the new last digit, adds all the digits as a string
        return str(num%10) + str(revNumber(num//10))
    
    
def isPrime(num,denominator): # uses 'denominator' to keep track of which number to divide by
    """determines whether the 1st number taken in is a prime number"""
    if num == 1:
        return False
    if denominator < math.sqrt(num): # end case
        return True 
    if num <=2: # end case
        return True
    
    if (num % denominator == 0): # if the denominator is a factor of the number
        return False
        
    else:
        if (isPrime(num, denominator-1)): # if the denominator is never a factor of the number
            return True
        else:
            return False # otherwise, the denominator is a factor at some point
    

def printPalindromePrimes(start, end):
    """calculates and prints all palindrome primes between the start and endpoint numbers"""
    if start > end: # end case 
        return
    else: 
        if(str(start) == revNumber(start) and isPrime(start, start-1)): # if the number 'start' is a palindrome and a prime
            print(start)
        printPalindromePrimes(start+1,end) # recurses
        
        
# prompts user to enter the starting and ending points then prints out the palindromic primes
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
printPalindromePrimes(start, end)