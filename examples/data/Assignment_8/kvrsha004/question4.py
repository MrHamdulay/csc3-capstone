""" Question 4 / Assignment 8: 0Palindromic prime finder
Shaheel Kooverjee - KVRSHA004
8 May 2014 """

import sys
sys.setrecursionlimit (30000)

def palindrome(string): #using palindrome function from question1.py
    if string == "": #base case where string is empty
        return True
    else:
        if string[0] == string[-1]: #if first and last characters are the same:
            return palindrome(string[1: -1]) #repeat function without first and last characters of string
    return False #not a palindrome if none of above are fully carried through

def prime_checker(n, div):#parameters: number, divisor
    if n == 1: #1 is not prime
        return False 
    if n%div == 0 and n>div: #false if n divisible by a number other than 1 and n, and if n greater than divisor
        return False
    if n>div and div<n**0.5: #check factors up to square root of n
        return prime_checker(n, div+1)
    return True #prime if none of above if-statements are true

def palindromicprime(n, m):
    if n == m:
        return
    else:
        if palindrome(str(n)) == True:
            if prime_checker(n, 2) == True:
                print(n) #print if prime and palindromic
                return palindromicprime(n+1, m) #repeat check process with n+1
            else:
                return palindromicprime(n+1, m)
        else: 
            return palindromicprime(n+1, m)
        
n = input("Enter the starting point N: \n")
if n != "":
    m = input("Enter the ending point M: \n")
    if m != "":
        n, m = eval(n), eval(m)
        print("The palindromic primes are: ")
        palindromicprime(n, m+1)