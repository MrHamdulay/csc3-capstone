# Yentl Naidu (NDXYEN001)
# 8 May 2014
# Assignment 8
# Question 4 - Palindromic primes using recursion

import math
import sys
sys.setrecursionlimit (30000) # Allows us to use higher values

def pal(s,test): # Takes in the variables "s" and test as parameters
    if(len(str(s))!=1): # If the number doesn't have only one digit
        d=s%10 # This calculates the last number 
        test=test+str(d) # Adds the last number to test
        return pal((s-(s%10))//10,test) 
    else:
        return(test+str(s))

def prime(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n)) # Gets the sqrt of function
    if(x!=(sq+1)): # If it is not the srqrt
        if(n%x!=0): # If it is divisible
            return prime(n,x+1,p) # Call function again
        else:
            return (p+"Not") # If it is not a prime
            
    
def method(n,m): 
    if n<=m:       # While n not equal to n
        tespPal=int(pal(n,"")) # Calls the pal function
        if tespPal==n: # If the number reversed == the number 
            testPrime=prime(n,2,"") # Calls the prime function
            if testPrime!="Not":
                print(n) # Prints the number
        method(n+1,m) # Calls the method of the next number
        
        
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    method(n,m)