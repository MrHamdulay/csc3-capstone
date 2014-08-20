import sys
import math
sys.setrecursionlimit (30000)
i=2
j=0

def check_palindrome(s):
    if s=="":
        return(True)
    
    elif s[0]==s[-1]:
        return(check_palindrome(s[1:-1]))
    
    else:
        return(False)

def checkprime(n):
    global i
    if n%i==0 and n>i:
        i=2
        return(False)
    if i>math.sqrt(n):
        i=2
        return(True) 
    if n > i:
        i+=1
        return checkprime(n)
    
def iterprimes(N,M):
    global j
    if j==0:
        j=N
        
    if j==1:
        j+=1
        
    if check_palindrome(str(j))==True:
        if checkprime(j)==True:
            print(j)
    if N<M:
        j+=1
        return(iterprimes(j,M))
    
N=eval(input("Enter the starting point N:\n"))

M=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
iterprimes(N, M)

    

