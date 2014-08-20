""" Palindromic prime using recursion
Tauhirah Eguardo
2014/05/09"""
import sys
import math
sys.setrecursionlimit (50000)

def main():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palin(N,M)   

def swapper(msg,revword):
    if msg == "":
        return revword
    else:
        revword += msg[-1] 
        msg = msg[:-1]
        return swapper(msg,revword)    

def prime_number(n,m):
    if n == 1:
        return False
    elif m<n:
        if n%m == 0:
            return False
        else:
            return prime_number(n,m+1)

def palin(start,end):
    #print(start)
    if start>end:
        return
    else:
        newword =""
        revword = swapper(str(start),newword)
        #print(revword)
        if revword == str(start):
            if prime_number(start,2) != False:
                print(start)
            else:
                pass
        else:   
            pass
        return palin(start+1,end)



main()