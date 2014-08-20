'''Prime check'''
import sys
sys.setrecursionlimit (30000)

z = 2
import math
def prime(M,z):
    if z > math.sqrt(M) +1:
        return 1
    elif M ==2:
        return 1
    elif M==1:
        return 0
    
    elif M % z !=0:
        return prime(M,z+1)
    else:
        return 0


#===========================================
'''check if a number is a palindrome'''
def palin(num):
    new = 0 
    
    old = num
    
    def pali(old,new):
        if old == 0:
            return new
      
        else:
            new = new*10 +(old%10)
            old = old//10
            return pali(old,new)
        
      
    if old==pali(old,new):
        return 'Palindrome'
    else: return 'not'
    
#===========================================================================
'''palindromic prime'''
def pp(M,N):
    n=M
    if n>N:
        return
    
    elif prime(M,z)==1:
            y =palin(M)
            if y == 'Palindrome':
                print(M)
    pp(M+1,N)
M = eval(input('Enter the starting point N:\n'))
N = eval(input("Enter the ending point M:\n"))
print('The palindromic primes are:')
pp(M,N)