''' Prime Palindrome
05/05/2014
Limpho Parkies'''

import math
import sys
sys.setrecursionlimit (30000)

N=eval(input('Enter the starting point N:\n'))
M=eval(input('Enter the ending point M:\n'))

def primes(num,fact):
    if num == 2:
        return True
    if num > 1:
        if fact<math.sqrt(num)+1:
            if num%fact==0:
                return False
            else:
                return(primes(num,fact+1))
        else:
            return True
           
def palin(pnum):
    if len(pnum)==1 or len(pnum)==0:
        return True
    else:
        if pnum[0]==pnum[len(pnum)-1]:
            return palin(pnum[1:len(pnum)-1])
        else:
            return False


def operate(N,M):
    if N<=M:
        if primes(N,2) and palin(str(N)):
            print(N)
            return operate(N+1,M)
        else:
            return operate(N+1,M)

print("The palindromic primes are:\n", end='')
operate(N,M)