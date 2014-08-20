"""
Prashanth Sridharan
SRDPRA001
Assignment 08
Question 04
"""
import sys
import math
sys.setrecursionlimit (30000)
#Variable n is the variable name for number defined for the parameter of the Reverse function
#Variable i is the variable defined for handling the string.
def Reverse(n):     
    i=str(n)
    if i=="":
        return i #Terminating step of the Reverse function
    else:
        return (Reverse(i[1:])+i[0])  #the recursive step of the Reverse function
def Prime_checkFuction(n, div=2):
    if n == 1: 
        return False
    else:
        if div>math.sqrt(n):         
            return True
        if n%div==0: 
            return False
        else:
            div+=1
            return Prime_checkFuction(n,div)   
def pPrime(k, l): #function defined for palindrome primes with integer parameters of k and l
    if(k!=l):
        if int(Reverse(k))==k: 
            if Prime_checkFuction(k):          
                return str(k) + "\n"+ str(pPrime(k+1,l))
            else:                
                return pPrime(k+1,l)
        else:   
            return pPrime(k+1,l)
    else:
        if int(Reverse(k))==k:
            if Prime_checkFuction(k):
                return k      
        else:
            return ""        
x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
print(pPrime(x,y)) #prints the palindromic primes