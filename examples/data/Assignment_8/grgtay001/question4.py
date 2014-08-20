""" palindromic primes using recursive functions
 tayla george
 9 may 2014"""

import math
import sys
sys.setrecursionlimit (30000) 

def pal(s,check): 
    if(len(str(s))!=1):              # If the number doesn't have only one digit
        d=s%10                       # Calculating the last number 
        check=check+str(d)           # Adds the last number to 'check'
        return pal((s-(s%10))//10,check) 
    else:
        return(check+str(s))

def primes(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n))            # Gets the square root
    if(x!=(sq+1)):                  # If it is not the square root
        if(n%x!=0):                 # If it is divisible
            return primes(n,x+1,p) 
        else:
            return (p+"Not")        # If it is not a prime
            
    
def func(n,m): 
    if n<=m:       
        tespPal=int(pal(n,"")) # Calls the pal function
        if tespPal==n: # If the number reversed == the number 
            testPrime=primes(n,2,"") # Calls the primes function
            if testPrime!="Not":
                print(n) 
        func(n+1,m) # Calls the func of the next number
        
        
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    func(n,m)