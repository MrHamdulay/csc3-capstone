"""A program to print out all the palindrome prime numbers between two variables
by Jeremy Smith SMTJER002
4 May 2014"""

import sys
sys.setrecursionlimit (30000)

def reverse(string):
    """reverses a string"""
    #stopping point is if there is no string left
    if len(string) == 0:
        return ""
    #return the last letter, plus the last letter of the rest of the string
    else:
        return string[-1] + reverse(string[0:-1])

def prime(number,start):
    """if a number is a prime number, returns True, else returns False"""
    if number == 1:
        return False
    elif number%start == 0 and number >= 2*start:
        return False
    #checks the mod of a number against an increasing value of the starting number, until the starting number is half the value of the number
    elif number >= 2 * start:
        return prime(number,start+1)
    else:
        return True
    
def palindrome(string):
    """Checks if a string is a palindrome, returns True if it is"""
    if reverse(string) == string:
        return True
    else:
        return False

def palin_primes(low, high):
    """Checks for all the prime numbers that are also palindromes between two numbers"""
    #stopping point is when the lower number is equal to the higher number
    if low >= high:
        if prime(high,2) == False:
            print(end="")
        #if the value for low is both a prime and a palindrome, prints the number
        elif prime(low,2) == True and palindrome(str(low)) == True:
            print(low)
    
    elif low < high:
        #if the value for low is both a prime and a palindrome, prints the number and continues the check with the next value of the range
        if prime(low,2) == True and palindrome(str(low)) == True:
            print(low)
            palin_primes((low+1),high)
        else:            
            palin_primes((low+1), high)
        

low = eval(input("Enter the starting point N:\n"))
high = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palin_primes(low,high)