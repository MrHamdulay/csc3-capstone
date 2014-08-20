# Program for outputting palindromic primes in a given range
# Lwazi Shezi
# 5 May 2014

import sys
sys.setrecursionlimit (30000)   # set recursion limit

def palindrome (string) :
    ''' Reverse the input string'''
    if len(string) == 1:
        return string
    else:
        first_letter = string[0]
        #the_rest = string[1:]
        string = palindrome(string[1:]) + first_letter
        return string

def prime_check (N,counter) :
    ''' Check whether a number is a prime or not'''
    # Base case, when the counter is equal to the number being evaluated (Then  the evaluated number is not a prime)
    if counter == int(N):
        if N != 2 :
            remainder = 0
            return False
        else: return True
    # Second base case, when the counter is one less the number being evaluated (Then the evaluated number is a prime)
    elif counter == (N-1):
        return True
    
    # If the base case hasn't been reached, increase the counter by one
    else :   
        remainder = N % counter
        if counter < N and remainder != 0:
            counter += 1
        
        # Once there is a number that goes to the evaluated number and doesn't leave a remainder, then the number is not a prime. Got to base case 1
        else:
            remainder == 0
            counter = N
        return prime_check(N,counter)

def pal_prime(N,M) :
    '''check whether a number is a palindromic prime, and output it'''
    # Base case, when the end point is equal to the start point
    if N == M :
        if prime_check(N,2) == True:
            N_reverse = palindrome(str(N))
            if N == int(N_reverse):
                print(N)
        else: print('',end = '')
     # Recursive step, when the current start point is a prime but not equal to the end point          
    elif N < M and prime_check(N,2) == True :
        N_reverse = palindrome(str(N))
        if N == int(N_reverse):
            print(N)
        N += 1
        return pal_prime(N,M)
    # Recursive step, when the current start point is not a prime and not equal to the end point           
    else: 
        N += 1
        return pal_prime(N,M)
    
N = eval(input('Enter the starting point N:\n'))
M = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
pal_prime(N,M)

    
