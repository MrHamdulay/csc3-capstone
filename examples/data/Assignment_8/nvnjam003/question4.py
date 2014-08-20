import sys
import question1
sys.setrecursionlimit (30000)

def isPrime (n, m): #Checking if prime    
    if n == 2 or n == 3:
        return True
    elif n%m == 0: #If divisible by m, not prime
        return False
    elif m > 2: #Then check smaller m
        return isPrime (n, m-1)
    else: #If none divide n, is prime
        return True
    
def smaller_palindromes (n, m):
    if n > 1 and question1.isPalindrome(str(n)) and isPrime(n, n//2) and n <= m: #If palindromic prime, and less than or equal m, print it
        print (n)
        smaller_palindromes (n+1, m) #Check bigger n
    elif n+1 <= m: #If n+1 still less than m, check it
        smaller_palindromes (n+1, m)
        
N = int(input("Enter the starting point N:\n")) #Printing the result
M = int(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
smaller_palindromes (N, M)
