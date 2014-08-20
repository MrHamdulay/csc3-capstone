import math
import question1 # Import apalindrom program from qeustion 1
import sys
sys.setrecursionlimit (30000)


def is_prime(y, divisor):
    if y < 2: #  Is not a prime number if less than 2
        return False
    
    elif y ==2:
        return True 
        
    elif math.sqrt(y) + 1 > divisor: 
        
        if y % divisor == 0:
            return False # Not prime as divisible wihtout remainder
        
        else:
            return is_prime(y, divisor + 1)
    else:
        return True
    
def counter(N, M):
    if N <= M:
        if is_prime(N, 2) and question1.palindrome(str(N)):
            print(N)
        counter(N+1, M)
        

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
counter(N, M)