"""Fionna Mautsa
aeeeeehhhh kljkflgjdfo
sigh
9th may 2014"""


import sys
sys.setrecursionlimit (30000)
import math
check1=0


def prime(n,count,check):
    
    if count>= math.sqrt(n):
        return check
    elif n%count==0:
        check +=1
        return prime(n,count+1,check)
    else:
        return prime(n,count+1,check)


check2 = True
def pali(name):
    global check2
    
         
    if name == '' or len(name)==1:
        if check2== True:
            return('Palindrome!')
    elif name[0]!=name[-1]:
    
        return('Not a palindrome!')
    else: 
        return pali(name[1:-1])

def pp(n,m):
    
    
    if n==m+1:
            return False    
    elif prime(n,1,0)>1:
        if pali(str(n))=='Palindrome!':
            print(n)
        return pp(n+1,m)
    else:
        return pp(n+1,m)
      
n =int(input('Enter the starting point N:\n') )
m =int(input('Enter the ending point M:\n'))
print('The palindromic primes are:\n')
pp(n,m)

        
    