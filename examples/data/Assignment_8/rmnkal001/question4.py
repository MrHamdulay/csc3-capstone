#Kalind Ramnarayan
#check if a string is a palindrome
#may 2014

import math
import sys
sys.setrecursionlimit (30000) 
def pal(s,test): 
    if(len(str(s))!=1): 
        d=s%10 
        test=test+str(d) 
        return pal((s-(s%10))//10,test) #calls the function again 
    else:
        return(test+str(s))

def prime(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n)) 
    if(x!=(sq+1)): 
        if(n%x!=0): 
            return prime(n,x+1,p) #call function again
        else:
            return (p+"Not") #return not a prime
            
    
def method(n,m): 
    if n<=m:       
        tespPal=int(pal(n,"")) # calls the pal function
        if tespPal==n:  
            testPrime=prime(n,2,"") #calls the prime function
            if testPrime!="Not":
                print(n) 
        method(n+1,m) #calls the method of the next number
        

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
method(n,m)
    
    
    