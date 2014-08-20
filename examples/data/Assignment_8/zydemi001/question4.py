""" A program that uses recursive functions to find all palindromic primes between two given integers
Author: Emiel Zyde
Date: 3 May 2014 """

import math
import sys
sys.setrecursionlimit (30000)

def palindrome_prime(m,n):    #this is the main function in the program, that combines the other two functions in order to achieve the objective of printing out the palindromic primes
    if m == n:
        return
    else:
        if palindrome(str(m)) == True:    #checks to see if it is a palindrome
            if prime_number(m,2,n) == True:   #checks to see if it is a prime number
                print(m)
                return palindrome_prime (m+1,n)
            else:
                return palindrome_prime (m+1, n)
        else:
            return palindrome_prime (m+1,n)

def prime_number(m, divisor,n):    #this is a function to check if a number is a prime number
    if m == 1:
        return False 
    if m % divisor == 0 and m > divisor:  #we are checking to see if m is divisble by any number that is smaller than it
        return False 
    if m > divisor and divisor < math.sqrt(n):  #conditions that allow the program to stop timeously 
        return prime_number(m, divisor+1, n)
    
    return True 

def palindrome(word):   #this is the program from question 1, re-used in this context
    if word == "":#base case 
        return True
    elif word[0] == " ":
        return palindrome(word[1:len(word)-1])
    elif word[0] == word[len(word)-1]:    #if the first and last characters of the word are the same, we "remove" them from the word and then check if the first and last characters of the new word are the same
        return palindrome (word[1:len(word)-1])
    
    return False 


#get input from the user and print out the palindromic primes 
m = input("Enter the starting point N:\n")
if m != "":
    n = input("Enter the ending point M:\n")
    if n != "":
        m = eval(m)
        n = eval(n)
        print("The palindromic primes are:")
        palindrome_prime(m,n+1)
