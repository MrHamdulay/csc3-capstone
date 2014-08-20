import math
import sys
sys.setrecursionlimit (30000)

def palindrome(number):
    number = str(number)
    if len(number) < 2:
        return True
    else:
        if number[0] == number[-1]:
            return palindrome(number[1:len(number) - 1])
        else:
            return False
        
def prime(number, i = 2):
    if number < 2:
        return False
    elif number == 2 or i > math.sqrt(number):
        return True
    elif number % i == 0:
        return False
    else:
        return prime(number, i + 1)

def check_both(N,M):
    if N == M:
        if palindrome(M) and prime(M):
            print(M)
    elif palindrome(N) and prime(N):
        print(N)
        check_both(N + 1, M)
    else:
        check_both(N + 1, M)
        
N = eval(input('Enter the starting point N:\n'))
M = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
check_both(N,M)

