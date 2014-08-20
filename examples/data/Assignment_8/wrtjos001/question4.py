"""find all palindromic primes between two given intervals using recursion
joshua wort
5 May 2014"""

import sys
sys.setrecursionlimit (30000)

import math

divisor=2
def prime_number(n,divisor,m):
    #checks special case of number=1
    if n==1:
        return False
    #checks if number is divisible by any numbers smaller than it
    if n%divisor==0 and n>divisor:
        return False
    if n>divisor and math.sqrt(m)>divisor:
        return prime_number(n,divisor+1,m)
    
    return True

def palindrome(number):
    #base case
    if number=="":
        return True
        
    elif number[0] == " ":
        return palindrome(number[1:len(number)-1])
        
    #checks if the first and last characters of the string are the same and if so will discard them and create a new string and continue the process of checking if the first and last characters are the same    
    else:
        if number[0]==number[len(number)-1]:
            return palindrome(number[1:len(number)-1])
            
    return False    
        
def palindromic_primes(n,m):
    if m==n:
        return
    else:
        if palindrome(str(n))==True: #checks if number is a palindrome
            if prime_number(n,2,m)==True: #checks if palindrome number is also a prime number 
                print(n)
            return palindromic_primes(n+1,m) 
        else:
            return palindromic_primes(n+1,m) 
               
n = eval(input("Enter the starting point N:\n"))
if n!="": #checks if a string has been inputted
    m = eval(input("Enter the ending point M:\n"))
    if m!="":
        print("The palindromic primes are:")
        palindromic_primes(n,m+1)
         