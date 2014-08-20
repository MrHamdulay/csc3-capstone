import math

import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

def is_palin(number):
    number = str(number)
    if len(number) < 2:
        return True #an empty or single-character string is palindromic
    else:
        if number[0] == number[-1]: #if first letter equals last letter, recursion happens
            return is_palin(number[1:len(number)-1])
        else:
            return False #if don't match, function ends with False.
    
def is_prime(num, div = 2): #divisor has default value of 2
    if num < 2:
        return False #less than 2 - not prime
    elif num == 2 or div > math.sqrt(num): #if divisor exceeds sqrt(num), number has no factors, therefore prime.
        return True
    elif num%div == 0: #number has a factor, therefore not prime
        return False
    else:
        return is_prime(num, div + 1) #divisor is incremented and recursion takes place
    
def main(N, M):
    if N == M:
        if is_palin(M) and is_prime(M): #M inclusive in test
            print(M)        
    elif is_palin(N) and is_prime(N): 
        print(N) #if both functions return True, number is palindromic prime
        main(N+1, M) #N is incrememnted and moves closer to M
    else:
        main(N+1, M)

print("The palindromic primes are:")
main(N, M)