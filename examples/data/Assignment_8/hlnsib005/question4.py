"""Name Sibulele Hlongwane
Date: 07 May 2014
Assignment: Determine Palindromic Prime numbers within a range of numbers
"""


import sys
sys.setrecursionlimit (30000)

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def Palindrome(m):
    s=str(m)
    #Base Case
    if len(s)<=1:
        return True
    else:
        #Checks to see if first character of string equals last chatacter of string
        if s[0]==(s[-1]): 
            #"new" string is put into palindrome function i.e: first and last characters are removed and palindrome function is recalled 
            return Palindrome(s[1:-1])
        #else if they do not match return false
        else:
            return False   

def ChecksPrime(n,m):
    #Base Case: If n reaches a point where its greater than m, "stop" recursion
    if n>m:
        return ""
    else:
    #Tests n if its divisible by the smallest prime numbers and if so then its not a prime number else return the incremented version of n
        if (n!=2) and (n%2)==0:
            return ChecksPrime(n+1,m)
        elif (n!=3) and (n%3) ==0:
            return ChecksPrime(n+1,m)
        elif (n!=5) and (n%5) ==0:
            return ChecksPrime(n+1,m)
        elif (n!=7) and (n%7) ==0:
            return ChecksPrime(n+1,m) 
        elif (n!=11) and (n%11) ==0:
            return ChecksPrime(n+1,m)       
        elif (n!=13) and (n%13) ==0:
            return ChecksPrime(n+1,m) 
        elif (n!=17) and (n%17) ==0:
            return ChecksPrime(n+1,m)     
        elif (n!=19) and (n%19) ==0:
            return ChecksPrime(n+1,m) 
        elif (n!=29) and (n%29) ==0:
            return ChecksPrime(n+1,m)  
        elif (n!=41) and (n%41) ==0:
            return ChecksPrime(n+1,m) 
        elif (n!=43) and (n%43) ==0:
            return ChecksPrime(n+1,m) 
        elif (n!=67) and (n%67) ==0:
            return ChecksPrime(n+1,m)    
        elif (n!=73) and (n%73) ==0:
            return ChecksPrime(n+1,m)  
        elif (n!=79) and (n%79) ==0:
            return ChecksPrime(n+1,m)
        elif (n!=83) and (n%83) ==0:
            return ChecksPrime(n+1,m)    
        elif (n!=101) and (n%101) ==0:
            return ChecksPrime(n+1,m)      
        elif (n!=109) and (n%109) ==0:
            return ChecksPrime(n+1,m)            
        else:
            #calls the palindrome function to check if n is a palindrome, and also to check if n is equal to 1 or not, else n+1
            if (Palindrome(n)==True) and (n!=1):
                print(n)
            return ChecksPrime(n+1,m)
      
            
 #displays list of palindromic prime numbers           
print(ChecksPrime(n,m))      
       