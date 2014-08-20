'''recursivle count pallendromic primes
nic findlay
08 may 2014'''
import math
import sys
sys.setrecursionlimit(30000)
import math

def prime(s,n):
    if s >= math.sqrt(n):
        return 1
    elif n % s == 0:
        return -1
    else:
        return (prime(s+1,n))
    
def palindrome(n):
    var = False
    n = str(n) 
    if len(n) == 0 or len(n) ==1:
        return var
    elif n[-1] == n[0]:
        n = n[1:-1]
        var = True
        return var + palindrome(n)
       
                
def main(n,s):
       
    if n == s:
        return '' 
    elif prime(2,n) == 1 and palindrome(n) == True:
        print(n)
        return main(n+1,s)
    else: return main(n+1, s)
      
var = True
n = int(input('Enter the starting point N:\n'))
s = int(input('Enter the ending point M:\n')) 
print('The palindromic primes are:')
i = 2
print(main(n,s))            
       