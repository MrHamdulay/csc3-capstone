"""program to find palindromic prime numbers
chris betteridge
07 may 2014"""

import math
import sys
sys.setrecursionlimit(30000)

N_starting = eval(input("Enter the starting point N:\n"))
M_ending = eval(input("Enter the ending point M:\n"))

def reverse (N_starting):
    #reverse string
    if N_starting == "":
        return N_starting
    else:
        return reverse(N_starting[1:]) + N_starting[0]

def is_prime(divisor, number):
    factors = 0
    if divisor > math.sqrt(number):
        return 0
    elif factors > 2:
        return 0
    elif number%divisor == 0:
        return factors + 1 + is_prime(divisor+1,number)
    else:
        return factors + is_prime(divisor+1,number)

def palin_primes(N_starting,M_ending):
    if N_starting > M_ending:
        return 0 
    else:
        if  is_prime(1,N_starting) == 1 and str(N_starting) == reverse(str(N_starting)) and N_starting != 1:
            print(N_starting)
            return palin_primes(N_starting+1,M_ending)
        else:
            return palin_primes(N_starting+1,M_ending)
        
print("The palindromic primes are:")
palin_primes(N_starting,M_ending)