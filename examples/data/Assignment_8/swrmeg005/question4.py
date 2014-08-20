#Program to print palindromic primes in a range
#By Megan Swartz
#12th May 2014

import sys
sys.setrecursionlimit(30000)

#checks if number is prime
def IsPrime(number,div):
    if number==1:
        return False
    if number==2:
        return True
    if number%div==0:
        return False
    elif div>=int(number**(1/2)):
        return True
    elif number%div!=0:
        return IsPrime(number,div+1)

#checks if number is palindromic
def palin(number):
    number=str(number)
    if len(number)<=1:
        return True
    elif number[0]==number[-1]:
        return palin(number[1:-1])
    else:
        return False

#does palindrome and prime checks for all numbers in n to m range
def checkrange(n,m):
    if n==m:
        return
    if IsPrime(n,div)==True and palin(n)==True:
        print(n)
        return checkrange(n+1,m)
    else:
        return checkrange(n+1,m)

#asks for user input then runs checks
div=2
n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
m+=1
print("The palindromic primes are:")
checkrange(n,m)