#question4
# Author: justin valsecchi
#2014/05/08


import sys # increasing the limit of the amount of recursions python will perform
sys.setrecursionlimit(30000)


def isPrime(p, count): #creating a function to find prime numbers
    if p == 1:
        return False
    elif count == int(p**(1/2)) + 1: #mathematical def. of a prime
        return True
    else:
        if p % count == 0:
            return False
        else:
            return isPrime(p, count + 1)


def reverse(p): #function to reverse a number
    return p if len(p) == 1 else p[-1] + reverse(p[:-1]) #reversing a number


def isPalindrome(p):
    if str(p) == reverse(str(p)):
        return True
    else:
        return False
palindromes = ''

def palindromicPrimes(start, end): # creating a function to find palindromes
    
    global palindromes
    if start == end: #checking to see if the 'first numebr' is equal to the 'last'
        if isPrime(start, 2) and isPalindrome(start):
            palindromes += str(start)
    else:
        if isPrime(start, 2) and isPalindrome(start):
            palindromes += str(start) + '\n'
            palindromicPrimes(start + 1, end)
        else:
            palindromicPrimes(start + 1, end)


n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromicPrimes(n, m)
print(palindromes)