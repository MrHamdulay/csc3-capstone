
import sys
sys.setrecursionlimit (30000)

n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))

b=1
def fact(b,n):
    if b==n+1:
        return 1
    elif n%b==0:
        return b* fact(b+1,n) 
    else:
        return fact(b+1,n)
        
        
print("The palindromic primes are:")

def palindrome(n):
    n=str(n)
    if len(n)==0 or len(n)==1:
        return "pali" 
        
    else:
        if n[0]==n[-1]:
            return palindrome(n[1:-1])
        else:
            return "nt"


        
def nothing(n):
    if n=='':
        return n
        
def plindrome_prime(n,m):
    if n!=m:
        prm=fact(1,n)
        if prm==n:
            if palindrome(n)=='pali' and  n!=1:
                    print(n)
        plindrome_prime(int(n)+1,m) 
plindrome_prime(n,m)
nothing(n)


if m==fact(1,m):
    if palindrome(m)=='pali':
        print(m)