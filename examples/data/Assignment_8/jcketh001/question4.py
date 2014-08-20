#Program to find palindromic primes
#Ethan Jackson
#9 May 2014

import sys
sys.setrecursionlimit (30000)

def palin(word):
    if word == '':#same function from question1
        return True
    else:
        if (ord(word[0]) - ord(word[len(word)-1])) == 0:
            return palin(word[1:len(word)-1])
        else:
            return False
        


def prime(number, den):
    if den>2 and number>1:
        if (number%(den-1))>0 and prime(number,den-1):#checks if number is prime
            return True#returns true if it is prime
        else: return False
    elif number>1:return True#one is not prime
    else: return False
    
def PrintPalinPrimes(N, M):
    if N <= M:
        if palin(str(N)):
            if prime(N, N):
                print(str(N))
        PrintPalinPrimes(N+1,M)
        

N = int(input("Enter the starting point N:\n"))
M = int(input("Enter the ending point M:\n"))  
print("The palindromic primes are:")
PrintPalinPrimes(N,M)
