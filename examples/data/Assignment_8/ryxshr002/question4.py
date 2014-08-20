"""Shriya Roy
8 May 2014
finding palandromic primes between 2 integers"""

import math
import sys
sys.setrecursionlimit (30000) 
def palindrome(num,T): #checks if palindrome
    N=len(str(num))
    if(N!=1): 
        T=T+str(num%10) 
        return palindrome((num-(num%10))//10,T) 
    else:
        return(T+str(num))

def prime(n,k):
    if(n==1):
        return "False"
    root=int(math.sqrt(n)) #gets the sqrt of function
    if(k!=(root+1)): 
        if(n%k!=0): 
            return prime(n,k+1) 
        else:
            return "False" 
            
    
def play(n,m): 
    if n<=m:       #within the range
        test1=int(palindrome(n,"")) 
        if test1==n:  
            test2=prime(n,2) 
            if test2!="False":
                print(n) 
        play(n+1,m) 
        
        

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
play(n,m)
    
          
            
        
         