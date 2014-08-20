__author__ = 'George de Kock'
"""program that uses recursive functions to find all palindromic primes between two integers supplied as input.
2014-05-05"""
import sys
sys.setrecursionlimit(30000)
import math


def prime(num, test):
    if (num%test == 0 or num == 1) and (num!=2):
        return False
    elif test+1 <= (math.sqrt(num)+1):
        return prime(num,test+1)
    else:
        return True

import question1

start = eval(input("Enter the starting point N:\n"))
end =  eval(input("Enter the ending point M:\n"))

def loop(start,end):
    if prime(start,2) and question1.testpalin(str(start)):
        print(start)

    if start != end:
        loop(start+1,end)


print("The palindromic primes are:")
loop(start,end)