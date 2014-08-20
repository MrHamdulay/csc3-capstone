"""Program that uses recursive functions to find all palindromic primes between two integers supplied as input
Telisha Ramlall
8 May 2014"""

import sys
sys.setrecursionlimit (30000)

def palindrome(n):
    #if one or no words left 
    n = str(n)
    if len(n) <= 1:
        return True
    
    #compare whether front and back characters are equal
    elif n[0] == n[len(n)-1]:
        return palindrome(int(n[1:len(n)-1]))
    
    else:
        return False
    
def prime_number(n, i):
    if i == n:
        return True
    
    elif (n % i != 0 and n>i):
        return prime_number(n, i+1)
    
def palindromic_primes(n, m):
  
    if (n > m):
        return "done"
    
    else:
        i = 2
        if palindrome(n) == True and prime_number(n, i) == True:
            print(n)
        palindromic_primes(n+1, m)
        

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_primes(n, m)