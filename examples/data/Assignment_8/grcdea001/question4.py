"""Program to find all the palindromic primes between two inputs provided by the user, using only recursion
Dean Gracey
5 May 2014"""
import math

import sys
sys.setrecursionlimit (30000)


def primepalin(start, end):
    """calls the isPrime function and the palindromic function for each value between min and max to find all palindromic primes"""
    w=1
    if start == 1:
        start+=1
    if start <= end:
        
        w = isPrime(start,2)
        if(w != 0 and palindromic(start)==True):
            print(start)
         
        
        primepalin(start+1,end);


def isPrime( n,checker):
    """checks if the given number is prime and takes in a checker (2) to determin if the number is prime"""
    if n%checker==0 and n!=2 and n!=checker:
        
        return(0)
    else: 
        if checker < math.sqrt(n): 
            return isPrime(n,checker+1)

    

def palindromic(num):
    """checks to see if a number is palindromic"""
    snum = str(num)
    
    if len(snum)<2:
        
        return True
    
    
    first = (snum[0])
    last = (snum)[(len(snum)-1)]

        
    if first!=last:
        return False         
        
    else:
        return palindromic(snum[1:len(snum)-1])    



start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
primepalin(start, end)


