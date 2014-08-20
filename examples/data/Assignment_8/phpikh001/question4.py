#Ikhlaas Pohplonker
#8 May 2014
#a program that finds all palindromic primes between two integers supplied as input
import sys
sys.setrecursionlimit (30000)
def palindrome(s):#recursion function to determine a palindrom
    if len(s)==1 or len(s)==0:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
def prime(x,i):#a function to dertermine a prime number
    if x==1 or x==0:
        return False
    elif x==2 or x==3:
        return True
    elif x%i==0 and i>1:
        return False
    elif i > 3:
        return prime(x,i-1)
    else:
        return True

def palindromic_primes(N,M):#recursion function that deterines a palindrome and prime number
    y=palindrome(str(N))
    i=N//2
    x=prime(N,i)
    if N==M+1:
        return 0    
    elif x==True and y==True:
        print(N)
        palindromic_primes(N+1,M)
        
    else:
        return palindromic_primes(N+1,M)
        
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromic_primes(N,M)    