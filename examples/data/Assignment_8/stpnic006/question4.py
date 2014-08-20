"""Program using recursive functions to find all palindromic primes between two integers supplied as input
Nicholas Stephenson
11 April 2014"""

import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

def numdrome(N): #"num"ber palin"drome" to reverse numbers
    return N if len(N) == 1 else N[-1] + numdrome(N[:-1]) 
    #As all single length numbers are "numdromes"
    #Second part rverses number

def ifdrome(N): #Function to check "if" plain"drome"
    if str(N) == numdrome(str(N)):
        return True
    else:
        return False
        #If same foward as backward return True, else (if not) return False
  
    
def ifprime(N, count): #Function to check if the suppliedinput is a prime number
    if N ==1: #1 is excluded from prime numbers as 1 is not a prime number (1/1=1)
        return False
    elif count == int(N**(1/2)) +1:
        return True
    else:
        if N % count == 0:
            return False
        else:
            return ifprime(N,count+1) #Recursion through all of input
        
palin =  "" #Create empty string where palindromic numbers will go
def primedrome(first, last):
    global palin #Acess variable outside of function
    if first == last: #If first number of function equals second
        if ifprime(first, 2) and ifdrome(first):
            palin += str(first)
    else: # If first number of function does NOT equals second
        if ifprime(first, 2) and ifdrome(first):
            palin+= str(first) + "\n"
            primedrome(first+1, last)
        else:
            primedrome(first+1, last)
            
            
print("The palindromic primes are:") #Header for the returned numbers (Which are palindromes)
primedrome(N,M) #calls and runs functions
print(palin)
#Prints the palindromes