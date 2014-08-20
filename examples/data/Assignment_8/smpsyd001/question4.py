'''Palindrome Numbers
6 May 2014
Sydney Simpson'''
import math
import sys
sys.setrecursionlimit (30000)

def is_prime(N,div):
    if div<2:
        return True
    else:
        if N%int(div)==0:
            return False
    return is_prime(N,div-1)

def palindrome(string,number):
    if len(string)==0:
        return string
    if number==len(string)-1:
        return string[number]
    else:
        new= palindrome(string,number+1)+string[number]
        return new
    
    

def main(N,M):
    if N>M:
        return
    div=(math.sqrt(N))
   
    if is_prime(N,div) == True and N!=1:
        new_N=N
        new=eval(palindrome(str(new_N),0))
        if new==(N):
            print(N)       
    return main(N+1,M)
    

N=input("Enter the starting point N:\n")
M=input("Enter the ending point M:\n")
print("The palindromic primes are:")
N=eval(N)
M=eval(M)
main(N,M)