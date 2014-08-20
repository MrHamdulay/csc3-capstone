#Palindromic Primes
#Sofia Palmer
#5 May 2014

import sys
sys.setrecursionlimit (30000)

N = input("Enter the starting point N:\n")
M = input("Enter the ending poing M:\n")
print("The palindromic primes are:")

N = eval(N)
M = eval(M)
            

def check_prime(N,x):
    if x < (N/2):
        if (N % x) == 0:
            return False
        else:
            return check_prime(N, x+1)
    else: 
        return True
                     

def reverse(N):
    N = str(N)
    if N == "":
        return N
    else:
        return reverse(N[1:]) + N[0]
    
    
def palin_primes(N,M):
    if N < (M-1):
        if (check_prime(N,2)): 
            if (str(N) == reverse(N)):
                print(N)
        return palin_primes(N+1, M)

palin_primes(N,M)
    
    
    