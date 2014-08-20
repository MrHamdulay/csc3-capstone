# anna borysova
# q2, ass8
# 2014 - 05 - 08
import math
import sys
sys.setrecursionlimit (30000)

def reverse(string, i=0):
    if i == len(str(string))-1:
        return str(string)[i]
    return reverse(string, i+1) + str(string)[i]

#is a number palindromic
def palin(string):
    if reverse(string) == str(string):
        return True
    else:
        return False

#is a number prime, i is 2    
def prime(num, i=2):
    if i > round(math.sqrt(num)):
        if num != 1:
            return True
        else:
            return False
    if num%i == 0:
        return False
    else:
        return prime(num, i+1)  

def palin_prime(num):
    if palin(num) and prime(num):
        return str(num) + "\n"
    else:
        return ""

#which numbers are palindromic primes  
def palin_primes(start, end):
    if start == end:
        return palin_prime(end)
    return palin_prime(start) + palin_primes(start + 1, end)

print("The palindromic primes are:\n"+palin_primes(int(input("Enter the starting point N:\n")), int(input("Enter the ending point M:\n"))), end="")
