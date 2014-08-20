'''A program that checks if a number is a palindrome and if it is a prime number
Jacob Ntesang
06 May 2014'''
from math import*
import sys
sys.setrecursionlimit (30000)


def palindrome(N):
    N = str(N)
    if len(N) <= 1:
        return True
    elif (ord(N[0]) - ord(N[len(N)-1])) == 0:
        return palindrome(N[1:len(N)-1])
    else:
        return False
               
def prime(N,d):
            if N == 1:
                        return False
                
            elif N == 2:
                        return True
            elif N % d == 0 and d <= ceil(sqrt(N)):
                        return False
            elif N % d == 0 and d == N:
                        return  True
            elif N % d != 0 and d <= ceil(sqrt(N)):
                        d += 1
                        return prime(N, d)
            elif N % d != 0 and d >= ceil(sqrt(N)):
                        return True
            elif N >1:
                        d += 1
                        return prime(N, d)    
def printing_out(N, M):
        d = 2
        if N <= M:
                if (palindrome(N) == True):
                        if prime(N,d) == True:
                                print(N)
                return printing_out(N+1, M)
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
d = 2
print("The palindromic primes are:")
printing_out(N,M)



    
    