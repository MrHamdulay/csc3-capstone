"""Check palindromic primes
Emmanuel Conradie
09 May 2014"""

import math

import sys

sys.setrecursionlimit (30000) 

#checks parameters
def pal(s,test): 
    if(len(str(s)) != 1):
        d = s%10 
        test += str(d)
        return pal((s-(s%10))//10,test) 
    else:
        return(test+str(s))

#check for prime
def prime(n,x,p):
    if(n == 1):
        return (p +"Not")
    sq = int(math.sqrt(n))
    if(x != (sq+1)): 
        if(n%x != 0): 
            return prime(n,x+1,p) 
        else:
            return (p + "Not")
            
#check if prime number is a palindrome    
def method(n,m): 
    if n <= m:      
        tespPal = int(pal(n,"")) 
        if tespPal == n:
            testPrime = prime(n,2,"") 
            if testPrime != "Not":
                print(n) 
        method(n+1,m) 
        
        
if __name__== "__main__":
    
    #parameter
    n=eval(input("Enter the starting point N:\n"))    
    m=eval(input("Enter the ending point M:\n"))
    
    #print palindromic primes
    print("The palindromic primes are:")
    
    method(n,m)