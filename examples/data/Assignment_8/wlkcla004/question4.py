"""palindromic prime finder
clare walker
5 may 2014"""
import math

import sys
sys.setrecursionlimit (30000)

def palin(string):
    if len(string)==1: #if at end, just return first letter
        return string
    else:
        return string[-1] + palin(string[:-1]) #reverse word

def palincheck(number): 
    """returns True if number is a palindrome, False if not"""
    if str(number) == palin(str(number)):
        return True
    else: 
        return False

def primecheck(number, divisor):
    """returns True if number is a prime number, False if not"""
    # make excpetions for number 1 and 2
    if number ==1:
        return False
    elif number ==2:
        return True
    #if divisor has reached sqaure root of number and no factor has been found, final prime decision is made
    elif divisor >= math.sqrt(number):
        if number%divisor==0: #if square root is a factor, then not prime
            return False
        else:
            return True # if all up to square root, and square root, are not factors, number is a prime
    elif number % divisor == 0: #factor found, thus not prime
        return False
    else: # carry on
        return primecheck(number, divisor +1)

def palinprime(N, M):
    """iterates through interval [N, M] and makes a string of palindromic primes each separated by a space"""
    if N==M:
        if palincheck(N) and primecheck(N,2):
            return str(N)
        else:
            return ""
    else:
        if palincheck(N) and primecheck(N,2):
            return str(N) + ' '+ palinprime(N + 1, M)
        else:
            return palinprime(N+1, M)

def printpp(pplist):
    """prints a given list with each item on a new line"""
    if len(pplist) ==1:
        return print(pplist[0])
    else:
        print(pplist[0])
        return printpp(pplist[1:])
    
    
def main(): #get and process inputs using functions
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    palinprimes=palinprime(N, M)
    pplist = palinprimes.split(' ') # turns string into a list that can be printed
    print("The palindromic primes are:")
    printpp(pplist)
    

if __name__ =="__main__":
    main()
    
