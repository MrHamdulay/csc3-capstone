"""Assignment 8 Question 4
James Lloyd
4 May 2014"""

import sys
sys.setrecursionlimit (30000)
import math
list = []

N = eval (input ("Enter the starting point N:\n"))
M = eval (input ("Enter the ending point M:\n"))
#Variable to assist with prime number function
count = 3

def prime (x, count):
    """Determines if a number is prime"""    
    #Setting Base case
     #Eliminating 0, 1 and multiples of 2 immediately
    if x == 0 or x == 1:
        return False 
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False    
    elif count > round (math.sqrt (x)):
        return True 
    else:
        if x == 3:
            return True
        elif x % count != 0:
            return prime (x, count + 2)
        else:
            return False
        
def prime_in_range (x, y):
    """Function to create a list of primes in a range"""
    #Setting base case
    if x > y:
        return list
    elif prime (x, count) == True:
        #Adding prime to list
        list.append (x)
        prime_in_range (x + 1, y)
    else:
        prime_in_range (x + 1, y)
        
def palindrome (string):
    """Recursive function to determine palindromes"""
    #Setting the base cases empty string, 1 and 2
    if string == '':
        return True
    if len (string) == 1:
        return True
    elif len (string) == 2:
        if string [0] == string [1]:
            return True
    #Checking if the first and last characters are equal and then removing them
    elif string [0] == string [-1]:
        return palindrome (string [1:-1])
    #Returning not if string fails all tests
    else:
        return False
        

#Recursive palindrome function
def palindrome_list (lists):
    """Function to print palindromes in a list"""
    #Setting the base case
    if lists == []:
        print ('',end = '')
    elif palindrome (str (lists [0])) == True:
        #Printing if true
        print (lists [0])
        palindrome_list (lists [1:])
    else:
        palindrome_list (lists [1:])
        
#Retrieving list of prime numbers
prime_in_range (N, M)
print ("The palindromic primes are:")
#Printing palindromes in list of prime numbers
palindrome_list (list)
 