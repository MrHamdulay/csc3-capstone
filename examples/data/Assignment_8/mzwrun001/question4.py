"""Program to check whether a number is a palindrome
Runako Muzwidzwa
07/05/2014"""
import math 
import sys
sys.setrecursionlimit (30000)


n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
d=2
x=""
palindrome_list=[]
print("The palindromic primes are:")
#to check if number is a palindrome
def check_palindrome(n):
    x=str(n)
    if len(x)<1:
        return True
    elif x[0]==x[-1]:
        x=x[1:-1]
        return check_palindrome(x)
    else:
        return False

#to check if palindrome is a prime number      
def check_prime(n,d):
    if n==1:
        return False
    
    if n ==0:
        return False
    
    if d>=2 and d<=round(math.sqrt(n)):#to make sure no floats are used
        if n%d==0:
            return False 
        else:
            return check_prime(n,d+1)
    else:
        return True

#to make a list of palindromic primes
def print_prime(n):
    if n<=n<=m: #to make sure the program only executes from n-m
        if check_palindrome(n) == True and check_prime(n,d) == True:
            palindrome_list.append(n)
            return print_prime(n+1)
        else: 
            return print_prime(n+1)
    else:
        return palindrome_list #function is now a list
#to print primes
c=print_prime(n)#to retain list
def print_list(c):
    if len(c) > 0:
        print (c[0])
        # print rest of list
        print_list(c[1:])
print_list(c)