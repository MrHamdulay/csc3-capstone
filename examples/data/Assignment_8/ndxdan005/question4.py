import math

import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

def palin(number):
    number = str(number)
    if len(number) < 2:
        return True 
    else:
        if number[0] == number[-1]: 
            return palin(number[1:len(number)-1])
        else:
            return False
    
def prime(num, div = 2):
    if num < 2:
        return False
    elif num == 2 or div > math.sqrt(num): 
        return True
    elif num%div == 0:
        return False
    else:
        return prime(num, div + 1)
    
def main(N, M):
    if N == M:
        if palin(M) and prime(M):
            print(M)        
    elif palin(N) and prime(N): 
        print(N)
        main(N+1, M)
    else:
        main(N+1, M)

print("The palindromic primes are:")
main(N, M)