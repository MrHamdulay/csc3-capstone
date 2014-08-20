"""Tevin Chetty
8 May 2014
Program to check for palindromic primes"""

import math #for squareroot
import sys
sys.setrecursionlimit (30000) #so that the program runs

def is_palindrome(check,reverse): #checks if a number is a palindrome
    string=str(check)
    if len(string)!=1: #for more than two digits
        reverse=reverse+str(check%10) #doing one digit at a time
        return is_palindrome((check-(check%10))//10,reverse)
    else:
        return (reverse+str(check)) # if one digit
        
def check_prime(N,divisor): #checking if it is a prime number
    if N==1: #one is not prime, base case
        return "no"
    check=(int(math.sqrt(N)))+1 #using squareroot method to check for prime
    if divisor!=check:
        if N%divisor!=0:
            return check_prime(N,divisor+1)
        else:
            return "no"
        
def run_function(N,M): #uses the above functions
    if N<=M: #the range
        testpalindrome=int(is_palindrome(N,"")) #as palindrome function returns a string
        if testpalindrome==N:
            testprime=check_prime(N,2)
            if testprime!="no": 
                print(N)
        run_function(N+1,M)


N=eval(input("Enter the starting point N: \n"))
M=eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
run_function(N,M) #runs function
    
    
    