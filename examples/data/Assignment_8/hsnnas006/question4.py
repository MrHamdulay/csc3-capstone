'''program to calculate palindromic primes using recursive functions
nasreen hoosain
07/05/14'''

import question1
import math
import sys
sys.setrecursionlimit (30000)

#function to check if number is prime
def accu_is_prime(m, factor):
    if m == 1: #1 is not prime
        return False
    elif factor == int(math.sqrt(m)) + 1: #if there are no factors up to including sqrt(m)
        return True
    elif m%factor == 0: #if there is a factor (other than 1)
        return False
    else: #try new factor
        factor += 1
        return accu_is_prime (m, factor)

def is_prime(m):
    return accu_is_prime (m, 2) #returns accu_is_prime with starting factor of 2
    
#function to check if prime is palindrome
def Palin_prime(n, m):
    if  n != m: #do while n not equal m
        if is_prime(n) == True and str(n) == question1.reverse(str(n)): #if it is prime and palindrome
            print(n, end ='\n')
            return Palin_prime(n+1, m) #increment n each time til n = m
        else: 
            return Palin_prime(n+1, m)
    else: #do if n = m
        if is_prime(n) == True and str(n) == question1.reverse(str(n)):
            return n   

if __name__ == '__main__':
    N = eval(input('Enter the starting point N:\n'))
    M = eval(input('Enter the ending point M:\n'))
    
    print('The palindromic primes are:')
    Palin_prime(N, M+1) #M+1 to include ending point