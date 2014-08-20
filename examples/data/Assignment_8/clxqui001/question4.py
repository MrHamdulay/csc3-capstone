"""this program finds first, all palindromic numbers between a specific interval then finds the prime numbers of the palindromes"""
import sys
sys.setrecursionlimit (300000)

def palindrome(string):
    """this function reverses a string"""
    if len(string)==0:
        return ""
    elif len(string)>=0:
        return palindrome(string[1:]) + string[0]
import math

def prime(val,div):
    """this function determines whether a number is a prime number or not"""
    if val<=1:
        return False
    if val==2:
        return True    
    if val%div==0:
        
        return False
   
    if div>math.sqrt(val):
        return True

    else:
        return prime(val,div+1)
    
    
                     
    
    
    
        
def palindromic_prime(m,n):
    """this function display all the numbers that a palindromes and prime numbers in the interval provided"""
    if m<=n :
        if palindrome(str(m))== str(m):
            if prime(m,2)== True:
                print(m)
                m+=1
                return palindromic_prime(m,n)
            else: return palindromic_prime(m+1,n)
                
        else: return palindromic_prime(m+1,n)
            
x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_prime(x,y)

  
    