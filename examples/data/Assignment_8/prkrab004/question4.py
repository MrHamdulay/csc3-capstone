#Assignment 9
#Question 4
#Rabia Parker
#Due Date: 09/05/14

#using recursion to find all palindromic primes between two intergers

import math #able to use math library
import sys #able to use more values and have a bigger limit
sys.setrecursionlimit (30000) 


def palindrome(A,check):
    if(len(str(A))!=1):
        B=A%10
        check=check+str(B)
        return palindrome((A-(A%10))//10,check)     
    else:
        return(check+str(A))
def primes(N,R,I):
    if N==1:
        return (N,"Not")
    root=int(math.sqrt(N))
    if (R!=(root+1)):
        if (N%R !=0):
            return primes(N,R+1,I)
        else:
            return (I+"Not")
        
def pal_primes(N,M):
    if N<=M:
        call_palindrome=int(palindrome(N,""))
        if call_palindrome==N:
            call_primes=primes(N,2,"")
            if call_primes!="Not":
                print(N)
        pal_primes(N+1,M)
            
if __name__=="__main__":
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    pal_primes(N,M)
      
 