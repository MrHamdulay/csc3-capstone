"""
Assignment 7 - Question 4
Program to identify all the palendremic prime numbers between a set interval
Jayan Smart
4 May 2014 - May the 4th be with you!
"""

from question1 import *
def prime(num,d):
    import sys
    sys.setrecursionlimit (30000)
    from math import sqrt
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0:
        return False
    elif num%d == 0:
        return False
    elif d >= (round(sqrt(num))+1):
        return True
    else:
        return prime(num, d+1)
def check(N, M):
    if N > M:
        return
    if str(N) == reverse(str(N)):
        if prime(N, 2):
            print(N)
            return(check(N+1, M))
        if prime(N, 2) == False:
            return check(N+1, M)
    else:
        return check(N+1, M)

    
def main():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    check(N, M)

if __name__ == "__main__":
    main()
