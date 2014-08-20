"""Find palindromic primes using recursion
Haaroon Cassiem
9 May 2014"""
import sys
import question1
import math
sys.setrecursionlimit (50000) #extend recursion limit

def prime(n,m):   
    #return true/false if a number is prime       
    if n==1:
        return False
    elif m>math.sqrt(n):
        return True  
    
    elif m<math.sqrt(n):
        if n%m==0:
            return False
        else:
            return prime(n,m+1)
        

def palin_primes(s,e):
    #print out palindromic primes
    
    if s==e:
        if prime(s,2):
            if str(s)==question1.reverse(str(s)):
                print(s)
            
    elif s<e:
        if prime(s,2):
            if str(s)==question1.reverse(str(s)):
                print(s)
        palin_primes(s+1,e)
#call functions
if __name__=="__main__":
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palin_primes(start,end)