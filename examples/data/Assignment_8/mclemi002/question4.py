"""emile mclennan
6/5/14
A8 Q4"""

import sys
sys.setrecursionlimit (30000)

def palindrome(s):
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            return palindrome(s[1:len(s)-1])
        else:
            return False
        
def prime(p, d):
    if p==1:
        return False
    elif d ==2:
        return True
    if p%(d-1) == 0:
        return False
    else:
        return prime(p, d-1)
    
def code(n,m):
    if n==m:
        return''
    else:
        if prime(n,n) == True and palindrome(str(n))==True:
            print(n)
            return code(n+1,m)
        else:
            return code(n+1,m)
    
N= eval(input('Enter the starting point N:\n'))
M=eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
print(code(N,M))