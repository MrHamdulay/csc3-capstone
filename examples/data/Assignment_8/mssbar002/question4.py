"""a program that uses recursive functions to find all palindromic primes 
between two integers supplied as input (start and end points are included)
05/05/2014
Barnett Msiska"""
import sys
sys.setrecursionlimit (30000)

def main():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palindromePrimes(N,M)

def palindromePrimes(N,M):
    """print numbers that are both primes and palindromes in the range(N,M) 
    inclusive of M"""
    if N == M:
        if isPrime(N, N-1) and isPalindrome(str(N)):
            print(N)
        else:
            return
    else:
        if isPrime(N, N-1) and isPalindrome(str(N)):
            print(N)
            palindromePrimes(N+1, M)
        else:
            palindromePrimes(N+1, M)
            
def isPrime(number, devisor):
    """Returns True if number is a prime and devisor is 1 less than number"""
    if number > 1:
        if devisor == 1:
            return True
        elif number%devisor == 0:
            return False
        else:
            return True and isPrime(number, devisor-1)
    
def isPalindrome(s):
    """return true if s is a palindrome"""
    if len(s)== 0:
        return True
    elif len(s) == 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])

main()