
# Purpose:     A program that uses recursive functions to find all palindromic primes between two integers supplied as input
# Author:      S.C.MDLALOSE
#
# Created:     08/05/2014
# Copyright:   (c) S.C.MDLALOSE 2014

#-------------------------------------------------------------------------------

import sys
sys.setrecursionlimit (30000)


N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

div=2

def prime (N, div):

    if (N)**0.5<div:
        if N!=1:
            return True
    elif N%div==0:
        return False
    else:
        return prime (N, div+1)


def reverse (N):
    if len(N)<2:
        return True
    elif N[0]==N[-1]:
        return reverse(N[1:-1])
    else:
        return False





def palindrome_nums (M, N):

    if N<=M:

        if reverse (str(N))==True:
            if prime (N, div)==True:
                    print (N)
                    palindrome_nums(M, N+1)
            else:
                palindrome_nums (M, N+1)

        else:
            palindrome_nums (M, N+1)

print("The palindromic primes are:")
palindrome_nums (M, N)

