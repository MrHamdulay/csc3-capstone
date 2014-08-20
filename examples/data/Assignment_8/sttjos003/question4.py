

import question1

import math

import sys
sys.setrecursionlimit (30000)

def checkprime(number,divisor):
    if number<=1:
        return False
    elif number==divisor:
        return checkprime(number,divisor-1)
    elif divisor==1:
        return True
    else:
        if number%divisor==0:
            return False
        else:
            return checkprime(number,divisor-1)

def printprimes(start,end):
    if start==end:
        start=str(start)
        if question1.check_palindrome(start):
            start=eval(start)
            divisor=round(math.sqrt(start))+1
            if checkprime(start,divisor):
                print(start)
         
    else:
        start=str(start)
        if question1.check_palindrome(start):
            start=eval(start)
            divisor=round(math.sqrt(start))+1
            if checkprime(start,divisor):
                print(start)
            printprimes(start+1,end)
        else:
            start=eval(start)
            printprimes(start+1,end)

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
printprimes(start,end)