import sys
sys.setrecursionlimit (30000)

#Thembekile Dubazana
#dbzphi002
#Assignment 8:Q4

import math
"""Palindromic Primes Recursion"""

#The inputs and variables
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

#The functions
def palin(N):
    N=str(N)
    if len(N) < 2:#This is where the palin will end
        return True
    else:
        if N[0]==N[-1]:#check first and last letters 
            return palin(N[1:-1]) #remove letters with each recursion
        
def prime(N,k):
    f=math.sqrt(N)#This is the value where the function will end
    if N==1:
        return False
    if k>f:
        return palin(N)#if no factor is found check if N a palindrome
    if N%k==0:
        return False
    else:
        return prime(N,k+1)#Check all factors  

def next(N,M):
    k=2
    answer=prime(N,k)#Where l
    if answer==True:
        print(N)#Print N if it is palindromic prime
    if N!=M:#Will end if N=M+1 so will recur numbers less than that
        return next(N+1,M)
          
#The results
print("The palindromic primes are:\n",end="")
next(N,M)
    


    
    