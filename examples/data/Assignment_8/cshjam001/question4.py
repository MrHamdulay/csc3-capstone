"""finding palindromic primes
James cushway
11-05-2014"""

import sys
sys.setrecursionlimit(30000)


def paliprime(x, y):
    if x > y:
        return True              
    x=str(x)
    if pali(x) == True:
        if prime(int(x), 2) == True:  
            print(x)
    paliprime(int(x) + 1, y)
    

def prime(x, z):
    if x == 1:            
        return False
    if x == 2:
        return True        
    if z > int(x**0.5)+1:  
        return True        
    if x%z == 0:           
        return False
    if z == 2:        
        z += 1
    else:
        z += 2
    return prime(x,z)

def pali(s):
    if len(s) < 2:   #single digits are palindromes
        return True
    if s[0] != s[-1]:  #if the 2 ends are not equal, then it is not a palindrome
        return False
    return pali(s[1:-1])   #otherwise check the next 2 ends if they do equal

x = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
paliprime(x, m)
