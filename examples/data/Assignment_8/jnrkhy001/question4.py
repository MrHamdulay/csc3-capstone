#Khyati Jinerdeb
#Assignment 8
#Date Submitted:09/05/2014
#program to find all plindromic primes between two integers

import math
import sys
sys.setrecursionlimit (30000)
sys.setrecursionlimit (30000) 



def palindrome(t,test): 
    if(len(str(t))!=1): #if the length of the string is not equal to 1
        d=t%10 
        test=test+str(d) #palindrome function
        return palindrome((t-(t%10))//10,test) 
    else:
        return(test+str(t))


def primenumber(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n)) #prime num function
    if(x!=(sq+1)): 
        if(n%x!=0): 
            return primenumber(n,x+1,p)
        else:
            return (p+"Not") 
            
    
def process(n,m): 
    if n<=m:      
        tespPal=int(palindrome(n,"")) 
        if tespPal==n:
            testPrime=primenumber(n,2,"") 
            if testPrime!="Not":
                print(n) 
        process(n+1,m) 
        
        
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    process(n,m)