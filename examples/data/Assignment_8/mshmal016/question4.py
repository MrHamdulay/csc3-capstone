import math
import sys
sys.setrecursionlimit (30000)
#check for prime
def prime2(p,m):
    if p == 1:
        return False
    elif m < 2:
        return True
    elif p%m == 0:
        return False
    else:
        return prime2(p,m-1)
        
def prime(N):
    return prime2(N,int(math.sqrt(N)))

#reverse number
def reverse(N):
    N=str(N)
    index=len(N)-1
    if len(N)==1:
        return N
    elif len(N)==0:
        return 0
    else:
        return N[index] + reverse(N[:index])
    
#check if number is palindrome
def check(N):
    N=str(N)
    if N!="":
        if N==reverse(N):
            return True
        else:
            return False
    elif N=="":
        return ""
    N=eval(N)
    
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def palinprime(N,M):
    if N<=M:
        if prime(N)==True and check(N)==True:
            print(N)
            return palinprime(N+1,M)
        else:
            return palinprime(N+1,M)
palinprime(N,M)


        
    