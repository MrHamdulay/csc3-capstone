'''program to check whether a number is a palindromic prime
Simangaliso Mlangeni
MLNSIM014
08 May 2014
Assignment 8, question 4'''

import sys
sys.setrecursionlimit (30000)#extends recursion limit

import math


def palindromeCheck(number):
    '''Function that checks whether a number is a palindrome or not'''
    number = str(number)#converts number to a string so that it can be reversable

    if len(number) ==1 or number=="":#any number that has a length of 1 is a palindrome(base case)
        return True
    elif number[0] != number[-1]:
        return False
    else:
        return palindromeCheck(number[1:-1])#converts string by reversing it


def primeCheck(startP,s):
    '''Function that checks whether a number is a prime number or not'''
    if startP == 1:
        return False
    elif s>math.sqrt(startP):
        return True
    elif startP%s == 0:#if number has any factors other than itself and 1, returns false
        return False
    else:
        return primeCheck(startP,s + 1)#recurses if above condition are not met


def palindromicP(startP,endingP):
    '''function that checks whether a number is a palindromic prime or not'''
    if startP > endingP:# base case that checks when the starting point has becasme bigger than ending point
        return ""
    elif palindromeCheck(startP):# checks whether number is a palindrome or not
        if primeCheck(startP,2):
            print(startP)# prints number if is a palindrome
            return palindromicP(startP + 1,endingP)#recurses and moves on to the next number
        else:
            return palindromicP(startP + 1,endingP)#if number is not a palindrome, moves on to next number 
    else:
        return palindromicP(startP + 1,endingP)#recurses over numbers if none of the above conditions are met 

#allows or requests values from user    
startP=eval(input("Enter the starting point N:\n"))
endingP=eval(input("Enter the ending point M:\n"))


print("The palindromic primes are:")
palindromicP(startP,endingP)
