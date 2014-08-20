# Author : Rayaan Fakier FKRRAY001
# Date : 08 - 05 - 2014
# question4.py

import math
import question1
import sys
sys.setrecursionlimit (30000)

def palin_prime_recurs(N, M):
    '''Recursive program that finds all palindromic primes between two integers'''
    # Base case - last check at M
    if N == (M+1):
        return
    # Recursive steps - checks if palindromic and calls prime_checker
    elif question1.recursive_palindrome(str(N)) == "Palindrome!":
        if prime_checker(3,N):
            print(N)
        return palin_prime_recurs(N+1, M)
    else:
        return palin_prime_recurs(N+1, M)
            
def prime_checker(num, N):
    '''Recursive program that checks if a number is prime'''
    # Base case - if it has a factor return False
    if N == 1:
        return False
    elif N == 2 or N == 3:
        return True
    elif (N % 2) == 0:
        return False
    elif N % num == 0:
        return False    
    # Check final case of sqrt(N)
    elif num == N//2:
        num = math.sqrt(N)
        return prime_checker(num+1, N)
    # Recursive step - check possible factors
    elif num < N//2:
        return prime_checker(num+1, N)
    # If none of the above, it must be a prime
    else:
        return True
if __name__ == '__main__':
    N = int(input("Enter the starting point N:\n"))
    M = int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")    
    palin_prime_recurs(N, M)