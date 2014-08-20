# This python program calculates palindromic primes using recursion
# A prime number is one that is only divisible by 1 and itself. 
# Examples are: 3, 11, 313,212, 44, 9009, 4567654
# Some examples of palindromic primes are: 11, 191, 313

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 09 May 2014

import sys
import question1 # Will use the string reversal recursion problem from this module
import math # Will use the square root function from this module
sys.setrecursionlimit (30000)

def palindrome(a,b):
    """returns a list of palindromic numbers in the range a to b recursively"""
    
    start,end = str(a),str(b) # Convert numbers to strings
    
    if a > b:
        return "" # Base case: Starting position bigger that the end position
    elif start == question1.reverse_recursion(start):
        return "\n" + str(start) + palindrome(int(a)+1,int(b)) # Number is a palindrome
    else:
        return palindrome(int(a)+1,int(b)) # Look at the next number


def divide_recursive(dividend,divisor):
    """Determines if the dividend has perfect factors between 2 and divisor"""
    if divisor == 1:
        return 1 # Base case: divisor is exactly 1
    elif dividend % divisor == 0:
        # Number has other divisors other than 1 and its self
        return 0 
    else:
        # Number has no divisor other than 1 and itself
        return 1 * divide_recursive(dividend,divisor-1)
        

def prime(n):
    """returns a string of prime numbers. Input to this function is a list"""
        
    if len(n) < 1:
        return "" # Base case: empty list
    elif int(n[0]) == 1:
        return prime(n[1:]) # 1 is not prime
    elif int(n[0]) == 2 or int(n[0]) == 3: # Save time here by not checking for factors        
        return "\n" + str(n[0]) + prime(n[1:]) # 2 and 3 are prime numbers    
    elif divide_recursive(int(n[0]),round(math.sqrt(int(n[0])),0)):
        # Use divide recursive to check if the number has factors between 2 and its square root
        return "\n" + str(n[0]) + prime(n[1:]) # Number is prime
    else:
        return prime(n[1:]) # Number is not prime, check the next number


def main():
    """prints out a list of all palindromic prime numbers"""
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    
    # Create a list of palindromes between N & M
    palindromes = palindrome(N,M).split("\n") 
    
    # Remove the first item which is a return character "\n"
    del palindromes[0] 
    
    # Remove palindromes that are not prime numbers
    primes = prime(palindromes)
    
    # Print out the list of palindromic prime numbers  
    print("The palindromic primes are:",primes)    
        
    
if __name__ == "__main__":
    main()

    
#Sample I/O:

#Enter the starting point N:
#200
#Enter the ending point M:
#800
#The palindromic primes are:
#313
#353
#373
#383
#727
#757
#787
#797