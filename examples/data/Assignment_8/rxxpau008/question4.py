#Finds palindromatic prime numbers between N and M
#Paul Roux - RXXPAU008
#08 May 2014

import sys
sys.setrecursionlimit (30000) #Used to increase the number of recursive steps allowed"

def check_palindrome(string):
    """Checks if a string is a palindrome by checking if the first
        and last letters of a string are the same using recursion by 
        removing the first and last character for each iteration.
        Returning true is it is a palindrome and false if it is not"""
    string = str(string)
    if string[0] != string[len(string)-1]:
        return False    
    else:
        if string[1:len(string)-1]:
            return check_palindrome(string[1:len(string)-1])
        else:
            return True
    
def check_prime(n,i):
    """Checks if a number is prime using trial division.
    Returns true if the number is a prime anf false if it is not"""
    if n==1: return False
    elif n==2: return True
    elif n==3: return True
    elif n%2==0: return False
    elif n%i==0: return False
    elif i<int(n**0.5)+1:
        return check_prime(n,i+2)  
    else: return True
    
def palindromatic_primes(start,end):
    """Finds the palindromatic primes between N and M by first checking if a 
    number is a palindrome and then whethor or not it is a prime"""
    if start <= end:
        if check_palindrome(start):
            if check_prime(start,3):
                    print(start)
                    palindromatic_primes(start+1,end)
            else:
                palindromatic_primes(start+1,end)
        else:
            palindromatic_primes(start+1,end)
               
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromatic_primes(start,end)