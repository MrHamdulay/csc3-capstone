"""
-GPXSHI001
-Ass8
-Q4

"""

import math

import sys

sys.setrecursionlimit (30000) #allows for higher numbers to be dealt with

def palindromic(T,test): 

    if(len(str(T))!=1): 

        s=T%10  

        test=test+str(s) 

        return palindromic((T-(T%10))//10,test) 

    else:

        return(test+str(T))



def prime(n,x,p):

    if(n==1):

        return (p+"Not")

    sq=int(math.sqrt(n)) 

    if(x!=(sq+1)): 

        if(n%x!=0): 

            return prime(n,x+1,p) #summons function 

        else:

            return (p+"Not")
            

    

def method(n,m): 

    if n<=m:      

        test=int(palindromic(n,"")) 

        if test==n:

            testPrime=prime(n,2,"") 

            if testPrime!="Not":

                print(n)

        method(n+1,m)

        
if __name__== "__main__":

    n=eval(input("Enter the starting point N:\n"))

    m=eval(input("Enter the ending point M:\n"))

    print("The palindromic primes are:")

    method(n,m)

    

    

    