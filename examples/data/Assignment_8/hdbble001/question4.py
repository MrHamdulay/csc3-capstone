"""blessings hadebe
print list of all palindromic primes between user inputed numbers #question4.py 
9 may 2014"""


import math
import sys
sys.setrecursionlimit (30000)

#checks if number is prime
def is_prime(X,Y):
    if Y<2:
        return False
    if X>math.sqrt(Y):
        return True #if a number is not divisible by any numbers between 2 and it's square root, it IS a prime number 
    elif Y % X==0:
        return False #if a number is divisible by any numbers other than itself and 1, it is not prime
    else:
        return is_prime(X+1, Y)   

#checks if string is palindrome    
def Palindrome(string):
    if string == '':
        return True
    elif string[0] == string[len(string)-1]:
        return Palindrome(string[1:len(string)-1])
    else:
        return False
#checks whether number is prime AND a palindrome
def check(N, M):
    if M+1==N:
        return ""
    else:
        if is_prime(2, N):
            if Palindrome(str(N)):
                print(N)
    return check(N+1, M)
       
        
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
check(N, M)