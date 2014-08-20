# program that uses recursive functions to find all palindromic primes between 
# two integers supplied as input (start and end points are included).
# Michele Balestra  BLSMIC004
# 7 May 2014

# to allow more recursion
import sys
sys.setrecursionlimit (30000)


def primeFact (n, div):
    '''function lists the factors of a number'''
    if n < div:
        return []
    if n % div == 0:
        return [div] + primeFact (n / div, 2)
    return primeFact (n, div + 1)


def palindrome(strnum):
    '''function determines if item is a palindrome'''
    if len(strnum)<1:
        return True
    else:
        if strnum[0] == strnum[-1]:
            return palindrome(strnum[1:-1])
        else:
            return False


def prime(n,m):
    '''function prints palindromic primes between 2 numbers'''
    if n==m:
        return ''
    elif len(primeFact(n,2)) == 1:
        if palindrome(str(n)):
            print(n)
        return prime(n+1,m)
    else:
        return prime(n+1,m) 

        
if __name__=="__main__":
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    prime(N,M+1)
    