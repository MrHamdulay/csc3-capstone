#A Program to find all palindromic primes between two integers supplied as input (start and end points are included).
#BRXCAI001
#09 May 2014

import math
import sys
sys.setrecursionlimit (30000)

#Get integer values.
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))


#Create a function to determine whether the values are palindromes.
def palindrome (integer):
    #Convert integer into a string.
    integer = str(integer)
    #If the string is only 1 or 2 characters it is a Palindrome.
    if len(integer) == 0 or len(integer) ==1 :
        return True
    #If the first letter of the string equals the last letter of the string then you move inward to check if the first and last letters correspond in the next string.
    elif integer[0] == integer[-1]:
        return palindrome(integer[1:-1])
    else:
        return False
    
#Create a function to determine whether the values are prime.
#Define first 'b'. 'b' must be one number less than 'a'.
def primecheck(b): 
    if b<=1:
        return False
    else:
        return prime(b,b-1) 
def prime (a,b):
    if b==1:
        return True
    else:
        #'a' is the number we are checking, 'b' is the divisior.
        #If 'a' can be divided by 'b' without a remainder it is not a prime.
        if a%b==0:
            return False
        else:
            #Minus one from b for each reiteration.
            return prime(a,b-1) 

#Create a function to determine whether the values are both palindromes and primes.        
def palindrome_prime (N,M):
    #Return an empty string ie. dont do anything when N equals M.
    if N > M:
        return '' 
    else:
        #If number is true for both a palindrome and a prime, return that number and then check the next number by iterating through the recursion.
        if primecheck(N) and palindrome(N):
            return str(N) +"\n"+ str(palindrome_prime(N+1,M)) 
        #If the number is not true for both then do not return it but check the next number by iterating through the recursion, ie. add 1 to N.
        else:
            return str(palindrome_prime(N+1,M)) 
        
print("The palindromic primes are:\n", palindrome_prime(N,M), sep= "", end = '')
    
    