"""program to find palindromic primes
Kristin Kinmont
4 May 2014"""
import math
import sys
sys.setrecursionlimit(30000)

def prime(start,x):
    if start == 2:
        return True
    elif start%2 == 0 or start == 1:
        return False
    elif x == 1:
        return True
    elif start%x == 0: # therefore is has a factor other than 1 and itself
        return False
    else:
        return prime(start,x-1)

def reverse (start):
    start = str(start)
    if start == "":
        return True
    if start[0] == start[-1]:
        return reverse(start[1:-1])
    else:
        return False
    
def pal_primes(start,end):
    x = round(math.sqrt(start))# x is used to determine what factors 'start' has 
    if start == end and prime(start,x):
        print(start)
    elif start != end:
        if reverse(start): 
            if prime(start,x):
                print(start)
                return pal_primes(start+1,end)
            else:
                return pal_primes(start+1,end)          
        else:
            return pal_primes(start+1,end)
        
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
pal_primes(start,end)
             