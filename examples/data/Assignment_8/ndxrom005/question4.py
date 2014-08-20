#Romello Naidoo
#NDXROM005
#9 May 2014
import math
import sys
sys.setrecursionlimit (30000)

def palindrome(s,test): 
    if(len(str(s))!=1): 
        d=s%10
        test=test+str(d) 
        return palindrome((s-(s%10))//10,test) 
    else:
        return(test+str(s))

def primeCheck(n,x,p):
    if(n==1):
        return (p+"N")
    sqr=int(math.sqrt(n)) 
    if(x!=(sqr+1)): 
        if(n%x!=0): 
            return primeCheck(n,x+1,p) 
        else:
            return (p+"N") 
            
    
def method(n,m): 
    if n<=m:      
        pal=int(palindrome(n,"")) 
        if pal==n: 
            primeTest=primeCheck(n,2,"") 
            if primeTest!="N":
                print(n) 
        method(n+1,m) 
        
        

    
    
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
method(n,m)
    
    
    