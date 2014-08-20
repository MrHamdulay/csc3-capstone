"""A recursive program to find all palindromic promes between two integers
Alison Hoernle
HRNALI002
4 May 2014"""

# increase the recursion limit
import sys
sys.setrecursionlimit (30000)

# A function to determine if a SINGLE number is a palindrome
def palindrome(num): 
    num = str(num) # make it a string to be able to slice
    if len(num) == 1: # base case if the number is one digit
        return True
    
    elif len(num) == 2: # easy to check a two digit number
        if num[0] == num[-1]:
            return True
        
    else: # recursion step
        if num[0] == num[-1]:
            if palindrome(num[1:-1]):
                return True
            else:
                return False
        else:
            return False

# A function to determine if a SINGLE number is prime  
def prime(num, divisor):
    
    if num == 1: # 1 is not prime
        return False
    
    if num == 2: # 2 is prime
        return True
    
    elif divisor == 2: # Base case: 2 is the last divisor to check
        if num % divisor != 0:
            return True
        else:
            return False
    
    else:
        if num % divisor != 0: # go through each divisor from one less than the number until it reaches the base case
            if prime(num, divisor - 1):
                return True
            else:
                return False
        else:
            return False

# A function to determine what numbers in between two integers are prime and palindrome       
def prime_palindrome(n, m):
    if n == m: # base case if you get to the last number in the list
        if palindrome(n) is True: # check if it's palindrome and then check if it's prime
            if prime(n, n-1) is True:
                return n
            else:
                return ''            
        else:
            return ''
    
    else:
        if palindrome(n) is True: # do the same for each value in the list until it reaches the upper limit (m)
            if prime(n, n-1) is True:
                return str(n) + '\n' + str(prime_palindrome(n+1, m))
            else:
                return str(prime_palindrome(n+1, m))            
        else:
            return str(prime_palindrome(n+1, m))
        
        
n = int(input("Enter the starting point N:\n"))
m = int(input("Enter the ending point M:\n"))
prime_palindromes = prime_palindrome(n, m)
print("The palindromic primes are:\n", prime_palindromes, sep = '')        